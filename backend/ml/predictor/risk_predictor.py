import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

class RiskPredictor:
    def __init__(self):
        self.model_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'models_saved')
        os.makedirs(self.model_dir, exist_ok=True)
        self.pregnancy_model_path = os.path.join(self.model_dir, 'pregnancy_risk_model.joblib')
        self.child_model_path = os.path.join(self.model_dir, 'child_risk_model.joblib')
        self.appointment_model_path = os.path.join(self.model_dir, 'appointment_risk_model.joblib')

    def train_initial_models(self):
        # Synthetic data for training
        # Pregnancy Risk: Age, Blood Pressure (Systolic, Diastolic), Previous Complications (Binary)
        X_preg = np.random.randint(18, 45, (100, 4))
        y_preg = np.random.randint(0, 3, 100) # 0: Low, 1: Medium, 2: High
        preg_model = RandomForestClassifier()
        preg_model.fit(X_preg, y_preg)
        joblib.dump(preg_model, self.pregnancy_model_path)

        # Child Health Risk: Birth Weight, Age (Days), Nutrition Score
        X_child = np.random.rand(100, 3)
        y_child = np.random.randint(0, 2, 100) # 0: Healthy, 1: At Risk
        child_model = RandomForestClassifier()
        child_model.fit(X_child, y_child)
        joblib.dump(child_model, self.child_model_path)

        # Appointment Risk: Previous Missed, Distance to Facility, Age
        X_app = np.random.rand(100, 3)
        y_app = np.random.randint(0, 2, 100) # 0: Likely to attend, 1: Likely to miss
        app_model = RandomForestClassifier()
        app_model.fit(X_app, y_app)
        joblib.dump(app_model, self.appointment_model_path)

    def predict_pregnancy_risk(self, age, systolic, diastolic, prev_complications):
        model = joblib.load(self.pregnancy_model_path)
        input_data = np.array([[age, systolic, diastolic, 1 if prev_complications else 0]])
        risk_score = model.predict_proba(input_data)[0]
        prediction = model.predict(input_data)[0]
        labels = ['LOW', 'MEDIUM', 'HIGH']
        return labels[prediction], float(np.max(risk_score))

    def predict_child_risk(self, birth_weight, age_days, nutrition_score):
        model = joblib.load(self.child_model_path)
        input_data = np.array([[birth_weight, age_days, nutrition_score]])
        risk_score = model.predict_proba(input_data)[0]
        prediction = model.predict(input_data)[0]
        labels = ['LOW', 'HIGH']
        return labels[prediction], float(np.max(risk_score))

    def predict_appointment_risk(self, prev_missed_count, distance, age):
        model = joblib.load(self.appointment_model_path)
        input_data = np.array([[prev_missed_count, distance, age]])
        risk_score = model.predict_proba(input_data)[0]
        prediction = model.predict(input_data)[0]
        labels = ['LOW', 'HIGH']
        return labels[prediction], float(np.max(risk_score))
