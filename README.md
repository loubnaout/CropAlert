# 🌾🚜  AgroExpert – CropAlert Platform 🌾🚜

AgroExpert is a collaborative web platform designed to connect **agronomists** and **farmers**. It enables real-time publication and reception of geo-tagged agricultural alerts, supporting effective crop management and rapid response to threats such as pests, diseases, and weather conditions.

---

## 🎯 Project Goal

Develop a real-time platform where:
- 🧑‍🌾 **Farmers** receive geolocated crop alerts
- 🧑‍🔬 **Agronomists** publish zone- and crop-specific alerts

---
### 🛠 Technology & User Experience Highlights

> 💡 **Stack:** Python ,Django, WebSocket , HTML5 , CSS, JavaScript (ES6+) - For all interactive functionality, Leaflet.js , OpenStreetMa

### ⚡ Real-time Communication

- **Real-time alert delivery** from agronomists → farmers
- **Instant notification system** without page refreshes
- **Efficient communication** for time-sensitive agricultural warnings

### ✨ Animated UI Features

✨ Animation & UX Improvements

- Smooth, functional animations for interactive elements and transitions

- Purposeful motion highlights alerts, map markers,

- Mobile-friendly animations with lightweight CSS, reduced motion support, and touch-optimized triggers'

- Animated Intro Sequence

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

## 📦 Instructions

- Run the App Locally (With WebSocket Server)
- Open your terminal and run:

- cd cropalert
- python server.py #or python3 server.py

Using your file explorer (not the terminal):
  - Navigate to the `cropalert/alerts` folder, then enter the `templates` directory.
  - Locate the alerts.html file, right-click it, and choose "Open with firefox" (or your preferred browser).
  - Copy the URL from the browser’s address bar
  - Open a new browser window.
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
3. Enter login credentials provided above

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

## 🔧 Troubleshooting  
### Common Issues

#### 🔐 Login Problems

- Ensure you're using the correct **username/password** combination  
- Verify you've selected the correct **role** (Farmer / Agronomist)  

#### 🗺️ Map Not Loading

- Check your **internet connection**  
- Ensure your **browser allows content** from OpenStreetMap  

#### 🚨 Alerts Not Received

- Verify the **WebSocket server is running** 
- Check if **browser notifications** are enabled  
- Look for the **notification badge** in the sidebar  

#### 📍 Location Services

- Ensure your **browser has location permissions**  
- Verify **device GPS is enabled** if using geolocation
  
📱 Mobile Compatibility

AgroExpert is fully optimized for mobile devices, offering a seamless user experience on smartphones and tablets. The responsive design ensures that all features—including maps, alerts, and real-time notifications—work smoothly across different screen sizes.



## 🎥 Live Demo

📽️ A short video demo showing real-time alert usage, geolocation, and farmer-agronomist interaction will be sent via email.
📧 Please check your inbox after reviewing this README.







