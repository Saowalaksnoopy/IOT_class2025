import os
import time
import json
import logging
from datetime import datetime

import cv2
from ultralytics import YOLO
from collections import defaultdict
import paho.mqtt.client as mqtt
from dotenv import load_dotenv

# ---------- Load environment ----------
load_dotenv(os.path.dirname(os.path.abspath(__file__))+"/.env")

MQTT_BROKER = os.getenv("MQTT_BROKER", "127.0.0.1")
MQTT_PORT = int(os.getenv("MQTT_PORT", "1883"))
MQTT_TOPIC = os.getenv("MQTT_TOPIC", "iot-object")
MQTT_QOS = int(os.getenv("MQTT_QOS", "0"))
CAMERA_ID = os.getenv("CAMERA_ID", "cam-01")  # camera id/student id

# ---------- Logging setup ----------
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    handlers=[
        logging.FileHandler("yolo_tracking.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("YOLO_Tracker")

# ---------- MQTT Setup ----------
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        logger.info("Connected to MQTT Broker!")
    else:
        logger.error(f"Failed to connect to MQTT Broker, return code {rc}")

mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect

try:
    mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
except Exception as e:
    logger.error(f"Initial MQTT connect failed: {e}")

mqtt_client.loop_start()

# ---------- Safe MQTT publish ----------
def mqtt_publish_safe(client, topic, payload, qos=0, max_retries=3, delay=2):
    for attempt in range(max_retries):
        try:
            result = client.publish(topic, payload, qos=qos)
            status = result.rc
            if status == 0:
                logger.info(f"MQTT Sent: topic: {topic} \n{payload}")
                return True
            else:
                logger.warning(f"MQTT publish failed with rc={status}, retrying...")
        except Exception as e:
            logger.error(f"MQTT publish exception: {e}, retrying...")

        # Try reconnect
        try:
            client.reconnect()
            logger.info("Reconnected to MQTT broker.")
        except Exception as e:
            logger.error(f"MQTT reconnect failed: {e}")

        time.sleep(delay)

    logger.error(f"Failed to publish after {max_retries} attempts: {payload}")
    return False

# ---------- YOLO Setup ----------
model = YOLO(os.path.dirname(os.path.abspath(__file__)) + '/yolo11l.pt')
class_list = model.names

# ---------- Video Input ----------
cap = cv2.VideoCapture(os.path.dirname(os.path.abspath(__file__)) + '/test_videos/4.mp4')
# Open the camera (0 is usually the default camera)
# cap = cv2.VideoCapture(0)  # built-in camera
# cap = cv2.VideoCapture(1)  # external webcam

if not cap.isOpened():
    logger.error("Cannot open video file")
    exit(1)

# ---------- Line for counting ----------
line_y = 430

# ---------- Data structures ----------
class_counts = defaultdict(int)
crossed_ids = set()

# ---------- FPS calculation ----------
prev_time = time.time()

# ---------- Main loop ----------
try:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            logger.info("End of video stream or cannot read frame.")
            break

        # YOLO tracking
        results = model.track(frame, persist=True, classes=[1,2,3,5,6,7], verbose=False)

        if results[0].boxes.data is not None:
            boxes = results[0].boxes.xyxy.cpu()
            track_ids = results[0].boxes.id.int().cpu().tolist()
            class_indices = results[0].boxes.cls.int().cpu().tolist()
            confidences = results[0].boxes.conf.cpu()

            # Draw counting line
            cv2.line(frame, (0, line_y), (frame.shape[1], line_y), (0, 0, 255), 3)

            for box, track_id, class_idx, conf in zip(boxes, track_ids, class_indices, confidences):
                x1, y1, x2, y2 = map(int, box)
                cx = (x1 + x2) // 2
                cy = (y1 + y2) // 2
                class_name = class_list[class_idx]

                # Draw bounding box and center
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.circle(frame, (cx, cy), 4, (0, 0, 255), -1)
                cv2.putText(frame, f"ID:{track_id} {class_name} {conf:.2f}", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)

                # Count and send MQTT if crossed line
                if cy > line_y and track_id not in crossed_ids:
                    crossed_ids.add(track_id)
                    class_counts[class_name] += 1  # cumulative count

                    payload = {
                        "timestamp": datetime.now().isoformat(),
                        "camera_id": CAMERA_ID,
                        "track_id": track_id,
                        "crossed_class": class_name,
                        "total_count": class_counts[class_name]
                    }
                    mqtt_publish_safe(mqtt_client, MQTT_TOPIC, json.dumps(payload), qos=MQTT_QOS)

            # Display counts on frame
            y_offset = 30
            for class_name, count in class_counts.items():
                cv2.putText(frame, f"{class_name}: {count}", (50, y_offset),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                y_offset += 30

        # Calculate FPS
        curr_time = time.time()
        fps = 1 / (curr_time - prev_time)
        prev_time = curr_time
        cv2.putText(frame, f"FPS: {fps:.1f}", (50, 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
        logger.debug(f"FPS: {fps:.1f}")

        # Show frame
        cv2.imshow("YOLO Object Tracking & Counting", frame)

        # Exit on 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            logger.info("User pressed 'q'. Exiting.")
            break

finally:
    cap.release()
    cv2.destroyAllWindows()
    mqtt_client.loop_stop()
    mqtt_client.disconnect()
    logger.info("MQTT disconnected and resources released.")
