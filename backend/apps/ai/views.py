from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pickle
import os
from .services import HealthAssistantService

class RiskPredictionView(APIView):
    def post(self, request):
        data = request.data
        # data format: {'age': 25, 'systolic_bp': 120, 'diastolic_bp': 80, 'hemoglobin': 12, 'previous_complications': 0}

        model_path = 'backend/ml/models/maternal_risk_model.pkl'
        if not os.path.exists(model_path):
            return Response({"error": "Model not found"}, status=status.HTTP_404_NOT_FOUND)

        with open(model_path, 'rb') as f:
            model = pickle.load(f)

        features = [[
            data.get('age'),
            data.get('systolic_bp'),
            data.get('diastolic_bp'),
            data.get('hemoglobin'),
            data.get('previous_complications')
        ]]

        prediction = model.predict(features)[0]
        probability = model.predict_proba(features)[0][1]

        return Response({
            "risk_score": int(prediction),
            "probability": float(probability),
            "category": "High Risk" if prediction == 1 else "Low Risk"
        })

class HealthAssistantView(APIView):
    def post(self, request):
        query = request.data.get('query')
        if not query:
            return Response({"error": "Query is required"}, status=status.HTTP_400_BAD_REQUEST)

        service = HealthAssistantService()
        advice = service.get_health_advice(query)

        return Response({"advice": advice})
