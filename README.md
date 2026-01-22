# EIC Management System

## Présentation

**EIC Management System** est un projet académique de conception et de développement
d'un système d’information réalisé dans le cadre des études en informatique/MIAGE.
L'objectif du projet est de modéliser, structurer et implémenter la gestion interne du
**Economic Ingenious Club (EIC)** à travers une approche méthodique mêlant:
conception SI, architecture logicielle et développement web.

---

## Objectifs du projet

- Comprendre et appliquer une démarche complète de conception SI
- Mettre en pratique la modélisation des données (MCD/MLDR)
- Structurer une application web autour de domaines métier clairs
- Préparer une implémentation backend avec Django
- Utiliser Docker pour standardiser l’environnement de développement

---

## Fonctionnalités ciblées

- Gestion des membres du club et de leurs rôles
- Organisation des cellules (Marketing, RH, Relations extérieures)
- Gestion des événements et du calendrier
- Communication interne (messages, rappels, avertissements)
- Gestion des contacts externes (partenaires, sponsors, formateurs)

---

## État d'd'avancement
Le système est actuellement fonctionnel sur les modules suivants :

- **Sécurité & Authentification :** Système complet de login/logout avec redirection sécurisée.
- **Tableau de Bord (Dashboard) :** Interface centrale affichant les statistiques clés et la navigation intuitive.
- **Gestion des Membres :** Modèle de données étendu (Profils) lié aux utilisateurs Django, permettant une gestion par Cellule.
- **Base de Contacts :** Répertoire dynamique des partenaires, entreprises et intervenants avec filtrage par type.
- **Calendrier des Événements :** Intégration de **FullCalendar JS** pour une visualisation interactive des réunions, formations et événements du club, synchronisée avec la base de données.
- **Messagerie Interne :** Système de communication permettant l'envoi et la réception de messages entre les membres du club.

---

## Choix d’architecture : apps métier Django

Le projet est structuré autour de **plusieurs applications Django métier** plutôt que
de simples pages HTML indépendantes.
Chaque application correspond à un **domaine fonctionnel précis** :

- membres: profils, rôles, statistiques, avertissements
- cellules: organisation interne du club
- evenements: événements et calendrier
- contacts: base de données des contacts externes
- messagerie: communication interne
- authentification: gestion des connexions et des permissions

Ce choix permet :

- une meilleure lisibilité du code
- une séparation claire des responsabilités
- une évolution plus simple du projet
  Créer une seule application globale aurait rendu le projet plus difficile à maintenir
  et moins fidèle à la modélisation du système d’information.

---

## Base de données

La base de données viens du MLDR
Les relations ont été implémentées dans django via:

- 'foreignKey' pour les cardinalités (1,N)
- 'ManyToManyField' pour els cardinalités (N,N)

---

## Conception du système d’information

La conception du projet repose sur:

- un **MCD (Modèle Conceptuel de Données)**
- un **MLDR (Modèle Logique de Données Relationnel)**
- un **script SQL** de création de la base de données

Les documents de conception sont disponibles dans le dossier: 'docs/MCD_MLDR.md'

---

## Installation et Lancement

1. Cloner le dépôt : 'git clone https://github.com/CHIBANE-Sarah/EIC-management-system.git'
2. Appliquer les migrations : 'python manage.py migrate'
3. Lancer le serveur : 'python manage.py runserver'