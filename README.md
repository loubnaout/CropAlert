# 🌾🚜  AgroExpert – CropAlert Platform 🌾🚜

AgroExpert is a collaborative web platform designed to connect **agronomists** and **farmers**. It enables real-time publication and reception of geo-tagged agricultural alerts, supporting effective crop management and rapid response to threats such as pests, diseases, and weather conditions.

---

## 🎯 Project Goal

Develop a real-time platform where:
- 🧑‍🌾 **Farmers** receive geolocated crop alerts
- 🧑‍🔬 **Agronomists** publish zone- and crop-specific alerts

---

> 💡 **Stack:** Python ,Django, WebSocket , HTML5 , CSS, JavaScript (ES6+) - For all interactive functionality, WebSocket, Leaflet.js , OpenStreetMap

---

## 🚀 Features

### 👥 Role-Based Access
- **Farmer Login:** `username=farmer`, `password=1234`  
- **Agronomist Login:** `username=agronomist`, `password=1234`

### 📲 Real-time Communication
- Instant alerts using WebSocket
- Persistent connection for dynamic updates

### 📌 Geolocation & Maps
- Mark your location using browser GPS  
- View alerts on an interactive OpenStreetMap-based map  
- Filter by distance, crop type, and alert type

### 🌱 Alerts System
- **Types:** Pest 🐛, Disease 🦠, Weather ☁️, Growth 🌾 , ..... 
- **Content:** Title, message, recommended actions, timestamp, and location

### 🧑‍🌾 Farmer Dashboard
- View incoming alerts with filters and timestamps  
- See detailed advice from agronomists  
- Track alerts by crop and region  

### 🧑‍🔬 Agronomist Dashboard
- Send custom alerts to farmers  
- Choose type, location, and affected crop  
- View alert history and update status  

---

## 📦 Installation

- Run the App Locally (With WebSocket Server)
- Open your terminal and run:

cd cropalert
python server.py

Using your file explorer (not the terminal):
  - Navigate to the cropalert/alertts folder.
  - Locate the alerts.html file, right-click it, and choose "Open with Chrome" (or your preferred browser).
  - Copy the URL from the browser’s address bar
  - Open a new browser window or a different browser.
  - Paste the copied URL to open a second instance of the app.

This way you can simulate both:

👨‍🌾 Farmer interface
👨‍🔬 Agronomist interface

![two-windows](https://github.com/user-attachments/assets/c7280c9c-3de5-412f-9877-f1184d3aa8f5)

## 📖 Usage Instructions

### 🔓 Authentication
1. Click **Get Started** on the animated intro screen
![intro](https://github.com/user-attachments/assets/ac5aed85-e4da-4959-a627-3c4b72278ccf)
2. Select your role: **Farmer** on one side, and on the other **Agronomist**
![choose-who](https://github.com/user-attachments/assets/d99ca208-029e-44d3-b28e-ce5d8572314e)
4. Enter login credentials provided above

**Farmer Login:** `username=farmer`, `password=1234`
**Agronomist Login:** `username=agronomist`, `password=1234`
![login](https://github.com/user-attachments/assets/544c0709-090e-44f9-81c6-3637ed8c71e7)
### 📡 Real-time Dashboard
- Farmers: Receive and view alerts
- Agronomists: Create and send alerts to specific zones
![Screenshot from 2025-06-23 13-02-26](https://github.com/user-attachments/assets/1938cd87-85de-496f-a140-06127c180469)

### 📍 Geolocation & Filtering
- View and filter alerts on an interactive map and create msg
- Click **Mark Location** to allow geolocation
![choose-agro](https://github.com/user-attachments/assets/acab5254-644c-4a3e-a45d-4503cd13b52d)
- send alert
![agro-farm-done](https://github.com/user-attachments/assets/fe41c1d0-f5b6-499e-b28d-4b5bbd2f84f9)

## ⚙️ Backend Integration


For full functionality, this frontend requires a WebSocket server running at ws://localhost:8767. The backend should:

Handle WebSocket connections

Manage user authentication

## 🎥 Live Demo

📽️ A short video demo showing real-time alert usage, geolocation, and farmer-agronomist interaction will be sent via email.
📧 Please check your inbox after reviewing this README.







