<div style="display: flex; justify-content: space-around; align-items: center;">
  <img src="https://github.com/marwin1991/profile-technology-icons/assets/76012086/24b02d77-2f28-43c7-b5d6-e15e3395851b" width="100px">
  <img src="https://user-images.githubusercontent.com/25181517/183423775-2276e25d-d43d-4e58-890b-edbc88e915f7.png" width="100px">
  <img src="https://user-images.githubusercontent.com/25181517/117207330-263ba280-adf4-11eb-9b97-0ac5b40bc3be.png" width="100px">
</div>

# Custom API BAN

Projet personnel de développement de endpoints API pour les données de la Base Adresse Nationale (BAN) avec des données à jour et un filtre par code insee dans le département 92.

## Description

Cette API permet de récupérer des données d'adresses à partir de la Base Adresse Nationale (BAN) en utilisant un code INSEE spécifique. Elle fournit également un endpoint pour vérifier si les données ont été mises à jour.

## Déploiement
Le premier lancement peut prendre quelques secondes supplémentaires en raison du démarrage du serveur après une période d'inactivité prolongée. Cela est dû au fait que le serveur s'éteint automatiquement après un certain temps d'inactivité pour des raisons de performances et de sécurité.

## Endpoints
- `GET /` : Affiche un message de bienvenue et les endpoints disponibles.
- `GET /<code_insee>` : Récupère les données pour un code INSEE spécifique.
- `GET /is_udpate` : Vérifie si les données ont été mises à jour cas spécifique pour les données à Meudon.

### Exemples d'utilisation
- Vérifier si les données ont été modifiées 
  ```sh
    https://dev-api-ban.onrender.com/is_udpate
  ```
- Afficher les données pour la Ville de Meudon 
  ```sh
    https://dev-api-ban.onrender.com/92048
  ```

## Installation en local avec Docker (pour les plus courageux)
Vous pouvez installer l'application sur vos serveurs facilement avec ces deux commandes docker (toutefois, assurez-vous que Docker). 


1. Construisez l'image Docker :
```sh
docker-compose build
```

2. Lancez le conteneur :
```sh
docker-compose up
```
