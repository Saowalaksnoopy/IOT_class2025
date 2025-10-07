# 📡 IoT Publisher

A Dockerized sample IoT publisher application that simulates sensor data and publishes it to a broker or stream processor (e.g., MQTT, Kafka).

```
iot-publisher/
├── app/
│   ├── Dockerfile
│   ├── main.py
│   ├── requirements.txt
│   └── Readme.md
├── .env
├── .gitignore
└── docker-compose.yml
```

---

## 🛠️ Prerequisites

Ensure the following tools are installed on your system:

* [Docker](https://docs.docker.com/get-docker/)
* [Git](https://git-scm.com/downloads)

---

## 🚀 Get the Application

Clone the repository using Git:

```bash
git clone https://github.com/hanattaw/Iot-class-2025-sensor
cd Iot-class-2025-sensor/iot-publisher
```

---

## ▶️ Run the Application

Start the application using Docker Compose:

```bash
docker compose up --build --remove-orphans
```

This will:

* Build the image (if not already built)
* Start the container
* Automatically remove any orphan containers

---

## 🧹 Stop & Remove the Application

To stop and clean up all associated volumes and containers:

```bash
docker compose down -v
```

---

Let me know if you'd like to include sample output, Kafka/MQTT configuration, or explanation of environment variables.
