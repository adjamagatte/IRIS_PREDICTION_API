# Projet MLOps : Classification avec une Régression Logistique

## Description

Ce projet illustre le cycle de vie d'un modèle de machine learning en production. Nous utilisons la régression logistique pour classer les fleurs du dataset Iris. Le projet inclut :

- L'entraînement du modèle avec `scikit-learn`.
- La sauvegarde du modèle et du scaler.
- Une API FastAPI pour servir les prédictions.
- Un déploiement sur un service gratuit (Render/Railway).

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
python -m venv venv  # Création de l'environnement
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
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

## API FastAPI (Bientôt)

Un fichier `main.py` sera ajouté dans `api/` pour servir le modèle via une API.

## TODO

✅ Entraînement du modèle\
✅ Sauvegarde du modèle\
✅ Test local des prédictions\
⬜ Implémentation de l'API\
⬜ Déploiement

---

**Auteur** : Adja

