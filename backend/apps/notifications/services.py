def send_fcm_notification(user, title, body, data=None):
    # Placeholder for FCM logic
    # In a real app, use firebase-admin SDK
    print(f"Sending FCM to {user.username}: {title} - {body}")
    return True

def trigger_sos(mother, lat=None, lng=None):
    # 1. Send SMS to predefined list (Placeholder)
    print(f"Sending SOS SMS for mother {mother.user.username}")

    # 2. Alert nearest facility
    facility = mother.user.facility
    if facility:
         print(f"Alerting facility: {facility.name}")

    # 3. Trigger push notifications to nearby health workers (Placeholder)
    print(f"Pushing SOS notification to health workers near {lat}, {lng}")
