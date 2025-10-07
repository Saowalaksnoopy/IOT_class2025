/*
* iot-class.ino
* iot-class from ESP32 Cucumber RIS with temperature, humidity, pressure, acceleration, angular_velocity, battery_voltage_mv (generate random)
* function: 
* 1. Connect to Wifi
* 2. Connect to MQTT
* 3. Publish data to MQTT for each sensor data
*/

#include <Wire.h>
#include <Adafruit_BMP280.h>
#include <Adafruit_MPU6050.h>
#include <SensirionI2cSht4x.h>
#include <PubSubClient.h>
#include <WiFi.h>
#include <ArduinoJson.h>

// Sensirion SHt4x
#define SDA_PIN 41
#define SCL_PIN 40
#define CLOCK_FEQ 100000
#define LED_BUILTIN 2 // LED Pin
SensirionI2cSht4x sht4x;

// NeoPixel
#include <Adafruit_NeoPixel.h>
#define LEDPIN 18
#define NUMPIXELS 1
Adafruit_NeoPixel pixels(NUMPIXELS, LEDPIN, NEO_GRB + NEO_KHZ800);
enum {NONE, RED, GREEN, BLUE};
int ledColor = NONE;

#define MQTT_BROKER   "192.168.1.104"
#define MQTT_PORT     1883
#define MQTT_USERNAME ""
#define MQTT_PASSWORD ""
#define MQTT_NAME     ""

// macro definitions
// make sure that we use the proper definition of NO_ERROR
#ifdef NO_ERROR
#undef NO_ERROR
#endif
#define NO_ERROR 0

//*** UPDATE THESE SETTINGS
// Wi-Fi settings - replace xxx with your Wi-Fi SSID and password
const char* ssid     = "LabIOT";
const char* password = "xxxxxxxxx";

// BPM280
Adafruit_BMP280 bmp;

// MPU6050
Adafruit_MPU6050 mpu;

static char errorMessage[64];
static int16_t error;

// Wifi
WiFiClient client;

// MQTT
PubSubClient mqtt(client);

// Setting up hareware
void setupHardware() {
    Wire.begin(SDA_PIN, SCL_PIN, CLOCK_FEQ);

    // Pixel setup
    pixels.begin();
  
    // prepare BMP280 sensor
    if (bmp.begin(0x76)) {
    Serial.println("BMP280 sensor ready");
    }

    // Sensirion setup
    Wire.begin(SDA_PIN, SCL_PIN, CLOCK_FEQ);
    sht4x.begin(Wire, SHT40_I2C_ADDR_44);
    if (bmp.begin(0x76)) {
      Serial.println("BMP280 sensor ready");
    }
    sht4x.softReset();
    delay(10);
    uint32_t serialNumber = 0;
    error = sht4x.serialNumber(serialNumber);
    if (error != NO_ERROR) {
      Serial.print("Error trying to execute serialNumber(): ");
      errorToString(error, errorMessage, sizeof errorMessage);
      Serial.println(errorMessage);
      return;
    }

    Serial.print("serialNumber: ");
    Serial.print(serialNumber);
    Serial.println();

  // prepare MPU6050 sensor
  if (mpu.begin()) { 
     Serial.println("MPU6050 sensor ready");
  }

  // configure a specific pin to behave either as an input or an output
  pinMode(LED_BUILTIN, OUTPUT);

  //write a HIGH or a LOW value to a digital pin
  digitalWrite(LED_BUILTIN, HIGH); 
}

void setup() {
  // Serial begin establishes serial communication between your Arduino board and another device.
  Serial.begin(115200);

  setupHardware();
  
  Serial.println("Starting");
  // if analog input pin 0 is unconnected, random analog
  // noise will cause the call to randomSeed() to generate
  // different seed numbers each time the sketch runs.
  // randomSeed() will then shuffle the random function.
  randomSeed(analogRead(0));

  // Initiate Wi-Fi connection setup
  WiFi.begin(ssid, password);

  // Show status on serial monitor
  Serial.print("\r\nConnecting to ");
  Serial.print(ssid); Serial.print(" ...");

  // Wait for Wi-Fi connection and show progress on serial monitor - blocking
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.print(" Connected! IP address: ");
  Serial.println(WiFi.localIP());

  // set mqtt server with server name and server port
  mqtt.setServer(MQTT_BROKER, MQTT_PORT);
}

void reconnect() {
  // Loop untill we're reconnected to mqtt server
  while(!client.connected()) {
    Serial.print("Attemping MQTT connection...");
    // Attemp to connect
    if (mqtt.connect(MQTT_NAME)){
      Serial.println("connected");
    }else {
      Serial.print("failed, rc=");
      Serial.print(mqtt.state());
      Serial.println(" try again in 5 seconds");

      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}

void loop() {
  static uint32_t prev_millis = 0;
  sensors_event_t temp;
  sensors_event_t a, g;

  char json[] = R"raw(
        {
            "id": "99999999",
            "name": "iot_sensor_99",
            "place_id": "32347983",
            "payload": {
                "temperature": -1,
                "humidity": 41,
                "pressure": 1023,
                // "timestamp": 1704225046,
                // "date": "2024-01-03T02:50:46+00:00",
            }
        })raw";

  DynamicJsonDocument doc(1024);
  deserializeJson(doc, json);

  // reconnect mqtt if disconnect
  if(!mqtt.connected()) {
    reconnect();
  }
  mqtt.loop();

  // read data for each 5 seconds.
  if ((millis() - prev_millis) > 5000) {
    prev_millis = millis();
    // read pressure data from BMP280
    float pressure = bmp.readPressure();

    // read temperature and humidity from SHT41
    uint16_t error;
    char errorMessage[256];
    float temperature;
    float humidity;
    error = sht4x.measureHighPrecision(temperature, humidity);
    if (error) {
      Serial.print("Error trying to execute measureHighPrecision(): ");
      errorToString(error, errorMessage, 256);
      Serial.println(errorMessage);
    }

    // read data from MPU6050 sensor
    mpu.getEvent(&a, &g, &temp);
    float ax = a.acceleration.x;
    float ay = a.acceleration.y;
    float az = a.acceleration.z;
    float gx = g.gyro.x;
    float gy = g.gyro.y;
    float gz = g.gyro.z;

    // random battery milli volt.
    unsigned int b = random(2900, 3000); 
  
    // publish data
  
    // doc["timestamp"] = epochTime;
    JsonObject payload = doc["payload"];
    payload["temperature"] = temperature;
    payload["humidity"] = humidity;
    payload["pressure"] = pressure;

    String jsonPayload;
    serializeJson(doc, jsonPayload);
    mqtt.publish("iot-frames-model", jsonPayload.c_str());

    Serial.println("Published sensor data to MQTT");
    Serial.println(jsonPayload);

  }
  
  switch (ledColor) {
        case NONE:
        pixels.setPixelColor(0, pixels.Color(0, 0, 0));
        pixels.show();
        break;

        case RED:
        pixels.setPixelColor(0, pixels.Color(20, 0, 0));
        pixels.show();
        break;

        case GREEN:
        pixels.setPixelColor(0, pixels.Color(0, 20, 0));
        pixels.show();
        break;

        case BLUE:
        pixels.setPixelColor(0, pixels.Color(0, 0, 20));
        pixels.show();
        break;

        default:
        break;
    }

    ledColor++;
    if (ledColor == 4) {
        ledColor = NONE;
    }
  delay(5000); // loop every 5 seconds
}