# 👋 Hi, I'm Masango Samuel

💻 Software Developer  
📍 Cameroon  

---

# Maternal and Child Health (MCH) Follow-Up System

This is a comprehensive, digital healthcare solution designed specifically for the Cameroonian context. It aims to bridge the gap in postnatal care and immunization tracking, especially in environments with limited internet connectivity.

## 📝 Project Description

In Cameroon, weak postnatal follow-up systems lead to missed maternal and child health visits, increasing preventable morbidity and mortality. This system replaces manual, paper-based tracking with a real-time digital record system that follows a mother from her first pregnancy checkup (ANC) through the child's early years.

### **Core App Features:**

#### **1. Role-Based Specialized Dashboards**
*   **Mothers:** A personal health companion to track pregnancy progress, receive automated appointment reminders, view child growth charts, and access a "one-tap" Emergency SOS button.
*   **Health Workers (Nurses/Doctors/CHWs):** A mobile tool to manage patient records in the field, record clinic visits, and receive automated alerts for high-risk patients.
*   **Administrators:** A system-wide view for managing health facilities, monitoring health statistics across regions, and managing user roles.

#### **2. Key Intelligent Features**
*   **AI Risk Prediction:** Uses machine learning (Random Forest) trained on synthetic Cameroonian health data to predict high-risk pregnancies and child malnutrition based on vitals like Blood Pressure, Weight, and Age.
*   **Offline-First Architecture:** The mobile app caches all data locally using SQFlite. When a health worker travels to a remote area without a signal, they can still record data. The system uses a "Smart Merge" logic to sync everything once a connection is restored.
*   **Real-Time Communication:** Integrated WebSocket-based chat allows mothers to consult directly with their assigned healthcare workers for non-emergencies.
*   **Bilingual Support:** Fully localized in both **English and French**, reflecting the official languages of Cameroon.
*   **WHO-Compliant Tracking:** Growth charts and vaccination schedules follow standard WHO guidelines (Weight-for-Age, Height-for-Age).

---

## 🛠️ Tech Stack

### 💻 Backend
- **Python / Django / DRF**: Robust REST API.
- **Django Channels**: WebSocket support for real-time chat.
- **Scikit-learn**: Machine learning risk prediction models.
- **PostgreSQL**: Production-grade database.

### 📱 Frontend
- **Flutter / Dart**: Cross-platform mobile application.
- **SQFlite**: Local database for offline caching.
- **Provider**: State management.

---

## 🚀 How to Launch the System

### Backend (Django)
1. **Docker (Recommended)**:
   ```bash
   docker-compose up --build
   ```
2. **Manual**:
   ```bash
   cd backend
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver
   ```

### Frontend (Flutter)
1. Install Flutter SDK.
2. Run the app:
   ```bash
   cd frontend
   flutter pub get
   flutter run
   ```

---

## 📫 Contact Me
- 📧 Email: masangosamuel78@email.com
- 💼 LinkedIn: https://www.linkedin.com/in/masango-samuel-5b9baa2a2?utm_source=share_via&utm_content=profile&utm_medium=member_ios

---

# 🐘 Laravel Version (XAMPP Support)

A parallel version of the backend has been implemented using **Laravel**, designed to work with **XAMPP/MySQL**.

## Setup Laravel
1. Go to `backend_laravel/`.
2. Follow instructions in `README_LARAVEL.md`.
3. The Flutter app can be configured to point to either the Django or Laravel backend by updating the `baseUrl` in service files.

## Features (Laravel)
- **Sanctum API Authentication**.
- **Eloquent Models** for all healthcare entities.
- **Python Bridge** for ML risk prediction.
