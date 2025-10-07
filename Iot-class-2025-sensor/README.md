# `README.md` IOT-CLASS-2025-SENSOR

```markdown
# 🌐 IoT Class 2025 — Sensor Simulation Project

This project provides a complete example of a simulated IoT data pipeline using Docker. It includes:

- **IoT Publisher**: Publishes sensor data (e.g., temperature, humidity) to a message broker (e.g., Kafka, MQTT).
- **IoT Subscriber**: Subscribes to the broker and processes or logs incoming sensor data.

---

## 🧭 Project Structure

Iot-class-2025-sensor/
├── iot-publisher/       # Publishes sensor data to broker
│   ├── app/
│   ├── docker-compose.yml
│   └── ...
├── iot-subscriber/      # Subscribes to broker and processes data
│   ├── app/
│   ├── docker-compose.yml
│   └── ...
└── README.md            # This file

````

---

## 🛠️ Prerequisites

Make sure you have the following installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Git](https://git-scm.com/downloads)

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/hanattaw/Iot-class-2025-sensor
cd Iot-class-2025-sensor
````

---

## 📡 Run IoT Publisher

```bash
cd iot-publisher
docker compose up --build --remove-orphans
```

To stop and remove:

```bash
docker compose down -v
```

More details in [`iot-publisher/README.md`](./iot-publisher/README.md)

---

## 📡 Run IoT Subscriber

```bash
cd iot-subscriber
docker compose up --build --remove-orphans
```

To stop and remove:

```bash
docker compose down -v
```

More details in [`iot-subscriber/README.md`](./iot-subscriber/README.md)

---

## 📦 Broker Configuration

The publisher and subscriber assume that a Kafka or MQTT broker is running. You can:

* Use your own external broker (set in `.env`)
* Or extend this project to include a broker container (e.g., `kafka-docker`, `emqx`)

---

## 📄 License

This project is part of the **IoT Class 2025** coursework. Feel free to fork or modify for educational use.

---