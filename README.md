# Maternal and Child Health (MCH) Follow-Up System

A complete cross-platform system for Cameroon to track mothers and children, send automated reminders, and predict health risks using AI.

## Project Structure

- `backend/`: Django REST Framework API with PostgreSQL.
- `frontend/`: Flutter Mobile Application.
- `ml/`: Scikit-learn Risk Prediction Module.

## Backend Setup (Docker)

1. Ensure Docker and Docker Compose are installed.
2. Run `docker-compose up --build`.
3. Access the API at `http://localhost:8000/api/`.

## API Documentation

- `POST /api/token/`: Get JWT Token.
- `GET /api/mothers/`: List mothers (Role restricted).
- `POST /api/risk-assessments/predict-pregnancy/`: Trigger AI risk prediction.

## Mobile App Setup

1. Install Flutter.
2. `cd frontend && flutter pub get`.
3. `flutter run`.

## AI Features

The system uses a Random Forest model to predict:
- High-risk pregnancies based on BP and history.
- Malnutrition risk in children.
- Missed appointment probability.
