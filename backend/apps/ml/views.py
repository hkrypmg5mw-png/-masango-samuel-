from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .utils import predict_risk

class RiskPredictionView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            data = request.data
            prediction, probability = predict_risk(data)
            return Response({
                'risk_score': probability,
                'is_high_risk': bool(prediction),
                'recommendation': 'Consult a specialist immediately' if prediction else 'Follow routine care'
            })
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
