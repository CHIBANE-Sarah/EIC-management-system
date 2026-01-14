# EIC Management System

## Présentation

**EIC Management System** est un projet académique de conception de système d’information
réalisé dans le cadre des études en informatique/MIAGE.
Il vise à modéliser et structurer la gestion interne du **Economic Ingenious Club (EIC)**.

---

## Fonctionnalités couvertes

- Gestion des membres et de leurs rôles
- Organisation des cellules du club
- Gestion des événements
- Communication interne (messages)
- Gestion des contacts externes

---

## Conception du système d’information

La conception repose sur:

- Un **MCD (Modèle Conceptuel de Données)**
- Un **MLDR (Modèle Logique de Données Relationnel)**
- Un **script SQL** pour la création de la base de données

---

## Structure du dépôt

EIC-management-systeme/
├─ docs/
│ ├─ MCD.png
│ ├─ MLDR.png
│ └─ MCD_MLDR.md
├─ sql/
│ └─ schema.sql
└─ README.md

---

## Documentation

La documentation complète des modèles de données est disponible dans:
'docs/MCD_MLDR.md'

---

## Base de données

Le fichier 'sql/schema.sql' permet de créer la base de données correspondant au MLDR.

---

## Évolution du projet

Ce dépôt constitue la **base de conception** du projet.
Il pourra être étendu ultérieurement avec:

- Une implémentation backend (Django)
- Une interface frontend
- Une base de données fonctionnelle
