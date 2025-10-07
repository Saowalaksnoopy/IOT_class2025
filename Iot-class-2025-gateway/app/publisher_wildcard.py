import paho.mqtt.client as mqtt
from datetime import datetime
import random
import time

BROKER = "172.30.15.133"
PORT = 1883

# 🔹 List of student IDs (each will get its own data stream)
STUDENT_IDS = [
    "6310301042",

]

# 🔹 Types of sensor data to simulate
SENSORS = ["temperature", "humidity", "pressure", "fan_speed"]

def timestamp():
    """Return current time as string (HH:MM:SS)."""
    return datetime.now().strftime("%H:%M:%S")

def generate_value(sensor: str):
    """Generate a random value depending on the sensor type."""
    if sensor == "temperature":
        return round(random.uniform(25, 35), 2)   # °C
    elif sensor == "humidity":
        return round(random.uniform(40, 70), 2)   # %
    elif sensor == "pressure":
        return round(random.uniform(1000, 1020), 2)  # hPa
    elif sensor == "fan_speed":
        return random.randint(0, 3)   # discrete levels 0–3
    else:
        return None

# 🔹 Callback to log client activity (useful for debugging)
def on_log(client, userdata, level, buf):
    print(f"[{timestamp()}] DEBUG | {buf}")

# 🔹 Callback when a publish has been acknowledged (QoS 1/2)
def on_publish(client, userdata, mid):
    print(f"[{timestamp()}] PUBLISHED | msgid={mid}")

# Create MQTT client
client = mqtt.Client()
client.on_log = on_log
client.on_publish = on_publish

# Connect to MQTT broker
client.connect(BROKER, PORT, 60)
client.loop_start()

try:
    while True:
        # Iterate through each student and each sensor
        for sid in STUDENT_IDS:
            for sensor in SENSORS:
                value = generate_value(sensor)  # create fake sensor data
                topic = f"test/qos/{sid}/{sensor}"  # topic for this student + sensor
                qos_level = 1  # QoS level (0 = at most once, 1 = at least once, 2 = exactly once)

                # Publish data
                result = client.publish(topic, str(value), qos=qos_level)

                # Print log to console
                print(
                    f"[{timestamp()}] PUBLISH REQUESTED | SID={sid} | "
                    f"{sensor}={value} | QoS={qos_level} | msgid={result.mid}"
                )

        # Wait before sending the next batch
        time.sleep(3)

except KeyboardInterrupt:
    print("Exiting...")
    client.loop_stop()
    client.disconnect()