from django.test import TestCase
from .utils import predict_risk

class MLModelTest(TestCase):
    def test_risk_prediction(self):
        data = {
            'age': 40,
            'systolic_bp': 150,
            'diastolic_bp': 95,
            'weight_kg': 80,
            'previous_complications': 1,
            'anc_attendance_count': 1
        }
        prediction, probability = predict_risk(data)
        self.assertEqual(prediction, 1) # Should be high risk
        self.assertGreater(probability, 0.5)

    def test_low_risk_prediction(self):
        data = {
            'age': 25,
            'systolic_bp': 110,
            'diastolic_bp': 70,
            'weight_kg': 60,
            'previous_complications': 0,
            'anc_attendance_count': 4
        }
        prediction, probability = predict_risk(data)
        self.assertEqual(prediction, 0)
        self.assertLess(probability, 0.5)
