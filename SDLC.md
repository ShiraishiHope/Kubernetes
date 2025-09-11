SDLC – Software Development Life Cycle

Projet : Application To-Do List avec Django, Docker et Kubernetes

1. Planification

Définition des besoins : une application web simple permettant d’ajouter, modifier, supprimer et valider des tâches.

Ajout d’un système de priorité, d’un historique et de filtres.

Déploiement prévu dans un environnement conteneurisé (Docker) puis orchestré avec Kubernetes.

Choix technologiques : Django (backend), SQLite (base de données légère), HTML/CSS (frontend minimal), Docker/Kubernetes (déploiement).

2. Analyse et Conception

Modélisation des données avec un modèle Task (titre, statut, priorité, date de création, date de complétion).

Définition de l’architecture MVC (Modèles, Vues, Templates) propre à Django.

Préparation de l’environnement de développement (virtualenv, requirements.txt, configuration de Dockerfile et docker-compose).

3. Développement

Création de l’application Django et configuration de la base de données.

Implémentation des vues : liste des tâches, ajout, modification, suppression, validation.

Création des templates HTML et d’un design simple mais clair.

Ajout des filtres et du tri (par priorité, statut, date).

Conteneurisation avec Docker pour assurer la portabilité.

4. Tests

Tests unitaires sur les modèles et les vues.

Tests manuels de l’interface web pour vérifier le bon fonctionnement des fonctionnalités.

Vérification de l’image Docker (build + run) et validation de l’accès via le navigateur.

5. Déploiement

Déploiement local avec Docker pour les tests.

Déploiement sur un cluster Kubernetes (Minikube ou Docker Desktop) pour simuler un environnement de production.

Documentation des commandes de déploiement et du fonctionnement de l’application.

6. Maintenance et Évolutions

Correction des éventuels bugs détectés après mise en production.

Optimisation du code et amélioration du design.

Ajout de nouvelles fonctionnalités si nécessaire (authentification, catégories de tâches, API REST).