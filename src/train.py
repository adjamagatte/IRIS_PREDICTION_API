import joblib
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import os

# Créer le dossier models s'il n'existe pas
os.makedirs("models", exist_ok=True)

def train():
    # Charger le dataset
    iris = load_iris()
    X = iris.data
    y = iris.target

    # Séparer les données
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Normalisation
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Entraînement
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)

    # Évaluation
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Précision du modèle : {accuracy:.2f}")

    # Sauvegarde
    joblib.dump(model, "models/iris_model.pkl")
    joblib.dump(scaler, "models/scaler.pkl")


if __name__ == "__main__":
    train()
