import logging
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Configurer le logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Charger le modèle et le scaler
model = joblib.load("models/iris_model.pkl")
scaler = joblib.load("models/scaler.pkl")

app = FastAPI()

class PredictionRequest(BaseModel):
    features: list

@app.get("/")
def home():
    return {"message": "Bienvenue sur l'API de prédiction d'Iris !"}

@app.post("/predict/")
def predict(request: PredictionRequest):
    # Récupérer les features depuis la requête
    features = np.array(request.features).reshape(1, -1)
    
    # Normalisation des features
    features_scaled = scaler.transform(features)
    
    # Prédiction
    prediction = model.predict(features_scaled)
    
    # Logger la requête et la prédiction
    logger.info(f"Prediction request: {request.features} => Prediction: {int(prediction[0])}")
    
    return {"prediction": int(prediction[0])}
