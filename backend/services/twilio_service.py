from django.conf import settings
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

class TwilioService:
    def __init__(self):
        self.client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        self.verify_sid = settings.TWILIO_VERIFY_SERVICE_SID

    def send_verification_code(self, phone_number):
        try:
            verification = self.client.verify.v2.services(self.verify_sid) \
                .verifications \
                .create(to=phone_number, channel='sms')
            return verification.status
        except TwilioRestException as e:
            print(f"Twilio Error: {e}")
            return None

    def check_verification_code(self, phone_number, code):
        try:
            verification_check = self.client.verify.v2.services(self.verify_sid) \
                .verification_checks \
                .create(to=phone_number, code=code)
            return verification_check.status == 'approved'
        except TwilioRestException as e:
            print(f"Twilio Error: {e}")
            return False
