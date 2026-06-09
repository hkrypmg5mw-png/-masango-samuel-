import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

def train_maternal_model():
    df = pd.read_csv('backend/ml/data/maternal_data.csv')
    X = df.drop('risk_level', axis=1)
    y = df['risk_level']
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X, y)
    joblib.dump(model, 'backend/ml/models/maternal_risk_model.joblib')
    print("Maternal risk model trained.")

def train_child_model():
    df = pd.read_csv('backend/ml/data/child_data.csv')
    X = df.drop('malnutrition', axis=1)
    y = df['malnutrition']
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X, y)
    joblib.dump(model, 'backend/ml/models/child_risk_model.joblib')
    print("Child risk model trained.")

if __name__ == "__main__":
    train_maternal_model()
    train_child_model()
