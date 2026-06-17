import firebase_admin
from firebase_admin import credentials, messaging
from django.conf import settings
import os

class FCMService:
    def __init__(self):
        if not firebase_admin._apps:
            # Assumes serviceAccountKey.json is provided in the root or via env
            cred_path = os.getenv('FIREBASE_SERVICE_ACCOUNT_PATH')
            if cred_path and os.path.exists(cred_path):
                cred = credentials.Certificate(cred_path)
                firebase_admin.initialize_app(cred)

    def send_push_notification(self, token, title, body, data=None):
        if not firebase_admin._apps:
            print("Firebase not initialized")
            return

        message = messaging.Message(
            notification=messaging.Notification(
                title=title,
                body=body,
            ),
            data=data,
            token=token,
        )
        try:
            response = messaging.send(message)
            return response
        except Exception as e:
            print(f"FCM Error: {e}")
            return None
