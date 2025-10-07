# 📟 `iot-class.ino` – IoT Sensor MQTT Publisher

This program runs on an **ESP32** with sensors from the **Cucumber RIS** board. It collects environmental and motion data and publishes it via MQTT in JSON format.

---

## 📋 Main Features

1. Connects to **Wi-Fi**
2. Connects to **MQTT Broker**
3. Reads sensor data from:

   * SHT41 (temperature & humidity)
   * BMP280 (pressure)
   * MPU6050 (acceleration & angular velocity)
   * Simulated battery voltage (randomized)
4. Publishes sensor data every 5 seconds in **JSON** format to MQTT
5. Displays status using **NeoPixel** (cycling through red, green, blue)

---

## 📦 Hardware Used

| Component        | Purpose                           |
| ---------------- | --------------------------------- |
| ESP32            | Main microcontroller              |
| SHT41            | Temperature & humidity sensor     |
| BMP280           | Atmospheric pressure sensor       |
| MPU6050          | Accelerometer + gyroscope         |
| NeoPixel (1 LED) | Status indicator                  |
| MQTT Broker      | Data collection (e.g., Mosquitto) |

---

## 🔌 I2C Pin Configuration

| Sensor                 | SDA | SCL |
| ---------------------- | --- | --- |
| SHT41, BMP280, MPU6050 | 41  | 40  |

---

## 🌐 Wi-Fi & MQTT Configuration

Make sure to set these values according to your environment:

```cpp
const char* ssid     = "LabIOT";
const char* password = "xxxxxxxxx";

#define MQTT_SERVER "192.168.1.104"
#define MQTT_PORT   1883
```

---

## 🧠 JSON Payload Structure

This is an example of the JSON structure published to MQTT:

```json
{
  "id": "99999999",
  "name": "iot_sensor_99",
  "place_id": "32347983",
  "payload": {
    "temperature": 30.15,
    "humidity": 45.3,
    "pressure": 101325,
    "timestamp": 1704225046,
    "date": "2024-01-03T02:50:46+00:00"
  }
}
```

---

## 🔁 Loop Behavior

Every 5 seconds:

1. Read data from SHT41, BMP280, MPU6050
2. Update the JSON payload
3. Publish the data to the MQTT topic: `iot-frames-model`
4. Cycle NeoPixel LED color

---

## 🌈 NeoPixel LED Status Indicators

| Color | Meaning              |
| ----- | -------------------- |
| Off   | Initial state        |
| Red   | Reading sensors      |
| Green | Publishing data      |
| Blue  | Waiting for next run |

---

## ⚠️ Notes & Warnings

* The JSON definition must **not contain `//` comments**, or it will fail to parse
* MPU6050 readings are **not included** in the published payload by default (can be enabled)
* You can add an NTP client to include real timestamp in the payload

---

