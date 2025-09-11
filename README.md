# Kubernetes To-Do List Project

Ce projet est une application To-Do List basée sur Django et SQLite, conteneurisée avec Docker. 

## Objectif

Créer une application de gestion de tâches avec les fonctionnalités suivantes :

- Ajouter, modifier et supprimer des tâches
- Marquer les tâches comme terminées
- Trier et filtrer les tâches par priorité et statut
- Déployer l'application dans un conteneur docker local

## Technologies

- Backend : Django (Python)
- Base de données : SQLite
- Conteneurisation : Docker
# (wip) - Orchestration : Kubernetes (Minikube ou Docker Desktop)
- Frontend : HTML/CSS simple

## Structure du projet

- `todo_list_app/` : Application Django principale
- `Dockerfile` : Fichier pour construire l'image Docker
- `db.sqlite3` : Base de données SQLite
- `manage.py` : Script principal de gestion Django
- `requirements.txt` : Dépendances Python
- `todo_list_project/` : Répertoire du projet Django

## Installation

### Prérequis

- Python 3.13+
- Docker

### Étapes

1. Cloner le dépôt :

   ```bash
   git clone https://gitlab.com/esgikubernetes/todo-list-project.git

2. Construire l'image Docker :

    docker compose up

3. Accéder à l'application via http://localhost:8000 
