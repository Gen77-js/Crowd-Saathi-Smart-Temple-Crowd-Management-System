# 🛕 Crowd Saathi – Smart Temple Crowd Management System

##  Overview

**Crowd Saathi** is an AI + IoT based real-time crowd monitoring and alert system designed for temples and large gatherings.
It helps prevent overcrowding, ensures safety, and enables smart crowd flow management.

---

## Problem Statement

Large gatherings in temples and public places often face:

* ❌ Sudden crowd surge
* ❌ Stampede risks
* ❌ Manual monitoring limitations
* ❌ Delayed emergency response

---

##  Solution

Crowd Saathi provides a **real-time intelligent monitoring system** that:

* Tracks crowd density using AI & sensors
* Detects high-risk zones instantly
* Sends alerts before danger occurs
* Provides live updates to users and admins

---

##  System Architecture

### 🔹 AI Camera Module

* Detects and tracks people using Computer Vision
* Provides real-time crowd count

### 🔹 IR Sensor + ESP32

* Entry/Exit tracking
* Accurate local counting
* Buzzer alert in high crowd situations

### 🔹 Backend (Flask)

* Data processing & fusion
* Crowd density calculation
* Zone classification (SAFE / MODERATE / ALERT)

### 🔹 Frontend (Android App)

* Live crowd status
* Heatmap visualization
* Voice alerts + notifications
* Graph trends

### 🔹 Admin Panel

* Zone-wise monitoring
* Team management
* Manual override system
* Live analytics

---

##  Features

### 👤 User App

* 🗺 Live Temple Map (Heatmap View)
* 📊 Crowd Trend Graph
* 🔊 Voice Alerts (TTS)
* 🔔 Notifications + Vibration
* 🚑 Medical Camp Info
* 📞 Emergency Helpline

###  Admin Panel

* Real-time zone monitoring
* RED zone highlighting
* Manual override (Force Alert / Safe Mode)
* Team assignment & contact

###  Hardware (ESP32)

* IR-based entry/exit counting
* LCD display
* Buzzer alert system

---

## 🛠 Tech Stack

### 💻 Software

* Python (Flask)
* OpenCV (AI Detection)
* Android (Kotlin)
* Retrofit API
* MPAndroidChart

### 🔌 Hardware

* ESP32
* IR Sensors
* I2C LCD
* Buzzer

---

## 🔗 API Example

```
GET /api/status

Response:
{
"total": 120,
"zones": {
"Z1": { "count": 40, "level": "GREEN" },
"Z2": { "count": 60, "level": "YELLOW" },
"Z3": { "count": 20, "level": "RED" }
},
"alerts": []
}
```

---

## ⚙️ Setup Instructions

### 🔹 Backend

```bash
pip install -r requirements.txt
python app.py
```

### 🔹 Android App

* Open in Android Studio
* Replace API base URL with your local IP
* Run on device/emulator

### 🔹 ESP32

* Update WiFi credentials
* Upload code using Arduino IDE

---

## 🌍 Real World Impact

* Prevents stampede situations
* Improves crowd flow
* Enhances public safety
* Enables smart event management

---

## 🔮 Future Scope

* Drone-based monitoring
* Predictive AI analytics
* Multi-language voice alerts
* Smart city integration


⭐ If you like this project, consider giving it a star!
