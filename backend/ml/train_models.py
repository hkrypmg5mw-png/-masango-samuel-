import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

def generate_synthetic_maternal_data(n_samples=1000):
    np.random.seed(42)
    age = np.random.randint(15, 45, n_samples)
    systolic_bp = np.random.randint(90, 160, n_samples)
    diastolic_bp = np.random.randint(60, 100, n_samples)
    hemoglobin = np.random.uniform(8, 14, n_samples)
    previous_complications = np.random.choice([0, 1], n_samples)

    # Simple risk logic for synthetic labels
    risk = ((systolic_bp > 140) | (diastolic_bp > 90) | (hemoglobin < 10) | (previous_complications == 1)).astype(int)

    df = pd.DataFrame({
        'age': age,
        'systolic_bp': systolic_bp,
        'diastolic_bp': diastolic_bp,
        'hemoglobin': hemoglobin,
        'previous_complications': previous_complications,
        'risk': risk
    })
    return df

def train_maternal_risk_model():
    df = generate_synthetic_maternal_data()
    X = df.drop('risk', axis=1)
    y = df['risk']

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)

    # Save model
    os.makedirs('backend/ml/models', exist_ok=True)
    with open('backend/ml/models/maternal_risk_model.pkl', 'wb') as f:
        pickle.dump(model, f)
    print("Maternal risk model trained and saved.")

if __name__ == "__main__":
    train_maternal_risk_model()
