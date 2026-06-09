from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import joblib
import pandas as pd
import os

MATERNAL_MODEL_PATH = 'backend/ml/models/maternal_risk_model.joblib'
CHILD_MODEL_PATH = 'backend/ml/models/child_risk_model.joblib'

class MaternalRiskPredictionView(APIView):
    def post(self, request):
        try:
            data = request.data
            features = pd.DataFrame([{
                'age': data['age'],
                'systolic_bp': data['systolic_bp'],
                'diastolic_bp': data['diastolic_bp'],
                'hb_level': data['hb_level'],
                'prev_complications': data['prev_complications']
            }])
            model = joblib.load(MATERNAL_MODEL_PATH)
            prediction = model.predict(features)[0]
            risk_map = {0: 'LOW', 1: 'MEDIUM', 2: 'HIGH'}
            return Response({'risk_level': risk_map[prediction]})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class ChildRiskPredictionView(APIView):
    def post(self, request):
        try:
            data = request.data
            features = pd.DataFrame([{
                'age_months': data['age_months'],
                'weight': data['weight'],
                'height': data['height']
            }])
            model = joblib.load(CHILD_MODEL_PATH)
            prediction = model.predict(features)[0]
            return Response({'malnutrition_risk': 'YES' if prediction == 1 else 'NO'})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class AIHealthAssistantView(APIView):
    def post(self, request):
        query = request.data.get('query', '').lower()
        responses = {
            'pregnancy': "During pregnancy, ensure you attend all ANC visits and take your iron supplements.",
            'vaccination': "Vaccinations protect your child from deadly diseases like Polio and Measles.",
            'nutrition': "Breastfeeding is recommended for the first 6 months of a child's life.",
            'emergency': "If you experience heavy bleeding or severe abdominal pain, contact your health facility immediately."
        }

        response_text = "I'm here to help with your maternal and child health questions. You can ask about pregnancy, vaccinations, or nutrition."
        for key in responses:
            if key in query:
                response_text = responses[key]
                break

        return Response({'response': response_text})
