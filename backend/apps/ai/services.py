import anthropic
from django.conf import settings

class HealthAssistantService:
    def __init__(self):
        self.client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)

    def get_health_advice(self, user_query, context=""):
        prompt = f"""You are an AI Health Assistant for the Maternal and Child Health Follow-Up System in Cameroon.
        Provide helpful, accurate, and culturally sensitive advice for mothers regarding pregnancy, child nutrition, and vaccinations.
        Context: {context}
        User Query: {user_query}
        """

        try:
            message = self.client.messages.create(
                model="claude-3-5-sonnet-20240620",
                max_tokens=1024,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            return message.content[0].text
        except Exception as e:
            print(f"Anthropic Error: {e}")
            return "I'm sorry, I cannot provide advice at the moment. Please consult a healthcare professional."
