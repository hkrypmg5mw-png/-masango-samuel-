import sys
import json
import os

# Add the django apps to path to use existing utils
sys.path.append(os.path.abspath('../backend'))
from apps.ml.utils import predict_risk

if __name__ == "__main__":
    if len(sys.argv) > 1:
        data = json.loads(sys.argv[1])
        prediction, probability = predict_risk(data)
        print(json.dumps({
            'risk_score': probability,
            'is_high_risk': bool(prediction),
            'recommendation': 'Consult a specialist immediately' if prediction else 'Follow routine care'
        }))
