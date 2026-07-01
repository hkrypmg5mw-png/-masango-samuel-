import anthropic
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class AIAssistantView(APIView):
    def post(self, request):
        user_query = request.data.get('query')
        if not user_query:
            return Response({"error": "Query is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)

            # System prompt to ensure medical safety and Cameroon context
            system_prompt = """You are a helpful Maternal and Child Health Assistant for mothers in Cameroon.
            Provide medical advice based on standard prenatal and postnatal care.
            Always advise consulting a doctor for serious symptoms.
            Include reminders about the Cameroon EPI vaccination schedule where relevant.
            Respond in the language of the query (English or French)."""

            message = client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=1024,
                system=system_prompt,
                messages=[
                    {"role": "user", "content": user_query}
                ]
            )

            return Response({"response": message.content[0].text})
        except Exception as e:
            # Fallback for when API key is missing or error occurs
            return Response({
                "response": "I'm currently undergoing maintenance. Please consult your local health center for immediate medical advice.",
                "debug_error": str(e) if settings.DEBUG else None
            }, status=status.HTTP_200_OK)
