import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

def generate_synthetic_data(n_samples=1000):
    np.random.seed(42)
    data = {
        'age': np.random.randint(15, 45, n_samples),
        'systolic_bp': np.random.randint(90, 160, n_samples),
        'diastolic_bp': np.random.randint(60, 100, n_samples),
        'weight_kg': np.random.randint(45, 120, n_samples),
        'previous_complications': np.random.choice([0, 1], n_samples, p=[0.8, 0.2]),
        'anc_attendance_count': np.random.randint(0, 8, n_samples),
    }
    df = pd.DataFrame(data)

    # Simple rule-based risk generation for synthetic target
    # High risk if BP is high or age is high or low attendance
    df['risk'] = 0
    df.loc[(df['systolic_bp'] > 140) | (df['diastolic_bp'] > 90), 'risk'] = 1
    df.loc[(df['age'] > 35) & (df['previous_complications'] == 1), 'risk'] = 1
    df.loc[(df['anc_attendance_count'] < 2) & (df['age'] > 30), 'risk'] = 1

    return df

def train_and_save_model():
    df = generate_synthetic_data()
    X = df.drop('risk', axis=1)
    y = df['risk']

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)

    model_path = os.path.join(os.path.dirname(__file__), 'risk_model.joblib')
    joblib.dump(model, model_path)
    return model_path

def predict_risk(data_dict):
    model_path = os.path.join(os.path.dirname(__file__), 'risk_model.joblib')
    if not os.path.exists(model_path):
        train_and_save_model()

    model = joblib.load(model_path)
    # Ensure data is in correct format/order
    features = ['age', 'systolic_bp', 'diastolic_bp', 'weight_kg', 'previous_complications', 'anc_attendance_count']
    input_data = [data_dict[f] for f in features]
    prediction = model.predict([input_data])
    probability = model.predict_proba([input_data])

    return int(prediction[0]), float(probability[0][1])
