# Projet MLOps : Classification avec une Régression Logistique

## Description

Ce projet illustre le cycle de vie d'un modèle de machine learning en production. Nous utilisons la régression logistique pour classer les fleurs du dataset Iris. Le projet inclut :

- L'entraînement du modèle avec `scikit-learn`.
- La sauvegarde du modèle et du scaler.
- Une API FastAPI pour servir les prédictions.
- Un déploiement sur un service gratuit (Render/Railway).
- La détection de drift des données et le réentraînement automatique du modèle si nécessaire.

## Structure du projet

```
mlops_project/
│── data/                     # Dossier pour stocker les données brutes (optionnel)
│── models/                   # Dossier pour stocker le modèle et le scaler
│   ├── iris_model.pkl        
│   ├── scaler.pkl            
│── src/                      # Scripts principaux
│   ├── train.py              # Entraînement du modèle
│   ├── preprocess.py         # Prétraitement des données
│   ├── predict.py            # Test des prédictions
│   ├── monitor.py            # Détection de drift et réentraînement
│── api/                      # API avec FastAPI
│   ├── main.py               # Endpoint pour les prédictions
│── notebooks/                # Notebooks pour l'exploration des données (optionnel)
│   ├── exploration.ipynb     
│── requirements.txt          # Liste des packages nécessaires
│── .gitignore                # Fichiers à exclure de Git
│── README.md                 # Explication du projet
```

## Installation

### 1️⃣ Créer et activer un environnement virtuel

```bash
python -m venv iris_venv  # Création de l'environnement
source iris_venv/bin/activate  # Linux/Mac
iris_venv\Scripts\activate  # Windows
```

### 2️⃣ Installer les dépendances

```bash
pip install -r requirements.txt
```

### 3️⃣ Entraîner le modèle

```bash
python src/train.py
```

### 4️⃣ Tester une prédiction

```bash
python src/predict.py
```

### 5️⃣ Lancer l'API

```bash
uvicorn api.main:app --reload
```

Accédez à l'API via [http://127.0.0.1:8000](http://127.0.0.1:8000)

## API FastAPI

Un endpoint `/predict` permet de soumettre des données et d'obtenir une prédiction.

Un endpoint `/` affiche un message de bienvenue.

## Monitoring et Data Drift

- Un script `monitor.py` détecte le drift des données.
- Si un drift est détecté, le modèle est réentraîné automatiquement.

## TODO

✅ Entraînement du modèle\
✅ Sauvegarde du modèle\
✅ Test local des prédictions\
✅ Implémentation de l'API\
✅ Détection de drift des données\
⬜ Déploiement

---

**Auteur** : Adja

