import pandas as pd
import numpy as np
import os

def generate_maternal_data(n=1000):
    np.random.seed(42)
    age = np.random.randint(15, 45, n)
    systolic_bp = np.random.randint(90, 160, n)
    diastolic_bp = np.random.randint(60, 100, n)
    hb_level = np.random.uniform(7, 14, n)
    prev_complications = np.random.choice([0, 1], n, p=[0.8, 0.2])

    # Simple logic for risk level
    risk_score = (systolic_bp > 140).astype(int) + (hb_level < 10).astype(int) + prev_complications
    risk_level = np.where(risk_score >= 2, 2, np.where(risk_score == 1, 1, 0)) # 0: Low, 1: Med, 2: High

    df = pd.DataFrame({
        'age': age,
        'systolic_bp': systolic_bp,
        'diastolic_bp': diastolic_bp,
        'hb_level': hb_level,
        'prev_complications': prev_complications,
        'risk_level': risk_level
    })
    return df

def generate_child_data(n=1000):
    np.random.seed(43)
    age_months = np.random.randint(0, 60, n)
    weight = np.random.uniform(2, 20, n)
    height = np.random.uniform(45, 110, n)

    # Simple logic for malnutrition (simplified weight-for-age)
    expected_weight = 3 + (age_months * 0.3)
    malnutrition = (weight < expected_weight * 0.7).astype(int)

    df = pd.DataFrame({
        'age_months': age_months,
        'weight': weight,
        'height': height,
        'malnutrition': malnutrition
    })
    return df

if __name__ == "__main__":
    os.makedirs('backend/ml/data', exist_ok=True)
    generate_maternal_data().to_csv('backend/ml/data/maternal_data.csv', index=False)
    generate_child_data().to_csv('backend/ml/data/child_data.csv', index=False)
    print("Synthetic datasets generated.")
