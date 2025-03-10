import joblib
import numpy as np

def predict(data):
    model = joblib.load("models/iris_model.pkl")
    processed_data = joblib.load("models/scaler.pkl").transform([data])
    prediction = model.predict(processed_data)
    return prediction[0]

if __name__ == "__main__":
    example_data = [5.1, 3.5, 1.4, 0.2]  # Exemple d'une fleur
    print(f"Prédiction : {predict(example_data)}")
