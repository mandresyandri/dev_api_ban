# Custom API BAN

Projet personnel de développement de endpoints API pour les données de la Base Adresse Nationale (BAN) avec des données à jour et un filtre par code insee dans le département 92.

## Description

Cette API permet de récupérer des données d'adresses à partir de la Base Adresse Nationale (BAN) en utilisant un code INSEE spécifique. Elle fournit également un endpoint pour vérifier si les données ont été mises à jour.

## Endpoints
- `GET /` : Affiche un message de bienvenue et les endpoints disponibles.
- `GET /<code_insee>` : Récupère les données pour un code INSEE spécifique.
- `GET /is_udpate` : Vérifie si les données ont été mises à jour cas spécifique pour les données à Meudon.

## Installation en local avec Docker (pour les plus courageux)
1. Construisez l'image Docker :
```sh
docker-compose build
```

2. Lancez le conteneur :
```sh
docker-compose up
```
