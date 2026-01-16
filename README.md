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

## Choix d’architecture : apps métier Django

Le projet est structuré autour de **plusieurs applications Django métier** plutôt que
de simples pages HTML indépendantes.
Chaque application correspond à un **domaine fonctionnel précis** :

- 'membres': profils, rôles, statistiques, avertissements
- 'cellules': organisation interne du club
- 'evenements': événements et calendrier
- 'contacts': base de données des contacts externes
- 'messagerie': communication interne
- 'authentification': gestion des connexions et des permissions

Ce choix permet :

- une meilleure lisibilité du code
- une séparation claire des responsabilités
- une évolution plus simple du projet

---

## Conception du système d’information

La conception du projet repose sur:

- un **MCD (Modèle Conceptuel de Données)**
- un **MLDR (Modèle Logique de Données Relationnel)**
- un **script SQL** de création de la base de données

Les documents de conception sont disponibles dans le dossier: 'docs/MCD_MLDR.md'

---
