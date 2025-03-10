from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Charger le modèle et le scaler
model = joblib.load("models/iris_model.pkl")
scaler = joblib.load("models/scaler.pkl")

app = FastAPI()

# Modèle Pydantic pour valider les entrées
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
    
    return {"prediction": int(prediction[0])}