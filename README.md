# Kubernetes To-Do List Project

Ce projet est une application To-Do List basée sur Django et PostgresSQL, conteneurisée avec Docker. 

## Objectif

Créer une application de gestion de tâches avec les fonctionnalités suivantes :

- Ajouter, modifier et supprimer des tâches
- Marquer les tâches comme terminées
- Trier et filtrer les tâches par priorité et statut
- Déployer l'application dans un conteneur docker local

## Technologies

- Backend : Django (Python)
- Base de données : PostgresSQL
- Conteneurisation : Docker
# (wip) - Orchestration : Kubernetes (Minikube ou Docker Desktop)
- Frontend : HTML/CSS simple

## Structure du projet

- `todo_list_app/` : Application Django principale
- `Dockerfile` : Fichier pour construire l'image Docker
- `volume persistant` : Base de données PostgresSQL
- `manage.py` : Script principal de gestion Django
- `requirements.txt` : Dépendances Python
- `todo_list_project/` : Répertoire du projet Django

## Installation

### Prérequis

- Python 3.13+
- Docker
- Minikube
- Kubectl

### Installation

1. Installation de Docker Desktop

Télécharger Docker Desktop depuis le site officiel :
https://www.docker.com/products/docker-desktop/

2. Installation de kubectl

kubectl est l’outil en ligne de commande utilisé pour interagir avec un cluster Kubernetes.

Télécharger la dernière version de kubectl.exe :
curl -LO "https://dl.k8s.io/release/v1.30.0/bin/windows/amd64/kubectl.exe"

3. Installation de Minikube

Minikube permet de créer un cluster Kubernetes local pour le développement et les tests.

Télécharger la version Windows de Minikube :
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-windows-amd64.exe

NOTE : Vérifiez que la version de Minikube utilisée est bien la même que celle indiquée dans le fichier deploy.bat et cleanup.bat
Le cas échéant mettre à jour le deploy.bat ainsi que le cleanup.bat


### Minikube
Déploiement automatisé avec deploy.bat
Description

Le fichier deploy.bat est un script d’automatisation permettant de déployer facilement une application Django (avec une base de données PostgreSQL) sur un cluster Kubernetes local via Minikube.

Au lieu d’exécuter chaque commande manuellement, ce script regroupe toutes les étapes nécessaires pour lancer l’environnement complet en une seule exécution.

Objectif

Le but de ce script est de :

Simplifier le déploiement local de l’application.

Éviter les erreurs humaines dues à l’exécution manuelle de commandes.

Garantir un ordre cohérent d’exécution des composants (base de données → migration → application → service).

Accélérer le cycle de développement et de test.

Fonctionnement étape par étape

Voici ce que fait le script deploy.bat :

1. Démarrage de Minikube
.\minikube-windows-amd64.exe start --driver=docker

2. Déploiement de PostgreSQL
kubectl apply -f postgres.yaml

3. Attente du démarrage de PostgreSQL
kubectl wait --for=condition=ready pod -l app=postgres --timeout=120s

4. Exécution du job de migration Django
kubectl apply -f job-migrate.yaml
kubectl wait --for=condition=complete job/todo-app-migrate --timeout=120s

5. Déploiement de l’application Django
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

6. Attente du pod Django
kubectl wait --for=condition=ready pod -l app=todo-app --timeout=120s

7. Ouverture de l’application dans le navigateur
.\minikube-windows-amd64.exe service todo-app-service

### Pour arrêter le service, utilisez le fichier cleanup.bat.