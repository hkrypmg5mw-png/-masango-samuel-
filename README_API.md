# MCH Follow-Up System API Documentation

## Authentication
- `POST /api/auth/register/`: Register a new user.
- `POST /api/auth/login/`: Login and receive JWT tokens.
- `GET /api/auth/profile/`: Get current user profile.

## Patient Management
- `GET /api/patients/mothers/`: List or create mothers.
- `GET /api/patients/children/`: List or create children.
- `GET /api/patients/pregnancies/`: List or create pregnancy records.

## Machine Learning
- `POST /api/ml/predict-pregnancy-risk/`: Predict pregnancy risk level.
  - Body: `{"age": 30, "systolic_bp": 145, "diastolic_bp": 95, "weight_kg": 75, "previous_complications": 1, "anc_attendance_count": 2}`

## Real-time Chat
- `WS /ws/chat/`: WebSocket endpoint for real-time messaging.

## Offline Sync
- Field-level smart merge is implemented on the backend to handle concurrent updates from mobile devices.
