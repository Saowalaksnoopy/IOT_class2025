import os
import paho.mqtt.client as mqtt
from datetime import datetime

# Load environment variables (optional)
from dotenv import load_dotenv
load_dotenv(os.path.dirname(os.path.abspath(__file__))+"/.env")
# load_dotenv(".env")

MQTT_BROKER = os.getenv("MQTT_BROKER", "127.0.0.1")
MQTT_PORT = int(os.getenv("MQTT_PORT", "1883"))
MQTT_TOPIC = os.getenv("MQTT_TOPIC", "iot-object-1234567890")

def timestamp():
    return datetime.now().strftime("%H:%M:%S")

# Callback เมื่อเชื่อมต่อ broker สำเร็จ (API v2)
def on_connect(client, userdata, flags, reason_code, properties=None):
    print(f"[{timestamp()}] Connected with reason_code={reason_code}")
    client.subscribe(MQTT_TOPIC, qos=0)  # subscribe ด้วย QoS สูงสุด

# Callback เมื่อรับข้อความจาก broker
def on_message(client, userdata, msg):
    print(f"[{timestamp()}] RECEIVED | QoS={msg.qos} | "
          f"Topic={msg.topic} | Message={msg.payload.decode()} | "
          f"msgid={getattr(msg, 'mid', 'N/A')}")

# Callback สำหรับ log debug
def on_log(client, userdata, level, buf):
    print(f"[{timestamp()}] DEBUG | {buf}")

# ใช้ API v2
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message
client.on_log = on_log  # เปิด debug log

client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.loop_forever()