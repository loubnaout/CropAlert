# 🌾 AgroExpert – CropAlert Platform

AgroExpert is a collaborative web platform designed to connect **agronomists** and **farmers**. It enables real-time publication and reception of geo-tagged agricultural alerts, supporting effective crop management and rapid response to threats such as pests, diseases, and weather conditions.

---

## 🎯 Project Goal

Develop a real-time platform where:
- 🧑‍🌾 **Farmers** receive geolocated crop alerts
- 🧑‍🔬 **Agronomists** publish zone- and crop-specific alerts

---

> 💡 **Stack:** Python , HTML5 , CSS, JavaScript (ES6+) - For all interactive functionality, WebSocket, Leaflet.js , OpenStreetMap – No framework used (client-side only)

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
  - Locate the index.html file, right-click it, and choose "Open with Chrome" (or your preferred browser).
  - Copy the URL from the browser’s address bar
  - Open a new browser window or a different browser.
  - Paste the copied URL to open a second instance of the app.

This way you can simulate both:

👨‍🌾 Farmer interface
👨‍🔬 Agronomist interface

## 📖 Usage Instructions

### 🔓 Authentication
1. Click **Get Started** on the animated intro screen  
2. Select your role: **Farmer** on one side, and **Agronomist** on the other**Agronomist**  
3. Enter login credentials provided above

### 📡 Real-time Dashboard
- Farmers: Receive and view alerts
- Agronomists: Create and send alerts to specific zones

### 📍 Location & Filtering
- Click **Mark Location** to allow geolocation  
- View and filter alerts on an interactive map

---

## ⚙️ Backend Integration

For full functionality, this frontend requires a WebSocket server running at ws://localhost:8767. The backend should:

Handle WebSocket connections

Manage user authentication

Route messages between farmers and agronomists


