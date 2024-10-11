# Utiliser une image de base officielle Python
FROM python:3.12-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de l'application
COPY . .

# Installer Poetry
RUN pip install poetry

# Installer les dépendances
RUN poetry install --no-dev

# Installer Gunicorn
RUN poetry add gunicorn

# Exposer le port sur lequel l'application va tourner
EXPOSE 5000

# Commande pour lancer l'application avec Gunicorn
CMD ["poetry", "run", "gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "main:app"]