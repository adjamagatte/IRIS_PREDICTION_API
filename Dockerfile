# Étape 1 : Utiliser une image Python officielle
FROM python:3.9-slim

# Étape 2 : Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Étape 3 : Copier le fichier requirements.txt pour installer les dépendances
COPY requirements.txt .

# Étape 4 : Installer les dépendances à partir de requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Étape 5 : Copier tous les fichiers du projet dans le conteneur
COPY . .

# Étape 6 : Exposer le port sur lequel l'application FastAPI sera lancée
EXPOSE 8000

# Étape 7 : Lancer l'application avec Uvicorn
CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8000"]


#docker build -t fastapi-iris-api .
# docker run -d -p 8000:8000 fastapi-iris-app

# 
