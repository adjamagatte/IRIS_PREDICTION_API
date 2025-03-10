import joblib
import numpy as np

def preprocess_data(data):
    scaler = joblib.load("../models/scaler.pkl")
    return scaler.transform(np.array(data).reshape(1, -1))
