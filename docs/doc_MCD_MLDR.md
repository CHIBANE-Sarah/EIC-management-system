# Documentation des modèles de données

## Projet : EIC Management System

---

## 1. Contexte du projet

Le projet **EIC Management System** vise à concevoir un système d’information permettant de gérer
le fonctionnement interne du club **Economic Ingenious Club (EIC)**.

Ce système permet:

- La gestion des membres du club
- L’organisation des cellules (Marketing, Management, RH, etc.)
- La gestion des événements
- La communication interne entre membres
- La gestion des contacts externes (partenaires, sponsors…)

Cette documentation présente :

- Le **MCD (Modèle Conceptuel de Données)**
- Le **MLDR (Modèle Logique de Données Relationnel)**

---

## 2. Modèle Conceptuel de Données (MCD)

![MCD](MCD.png)

### 2.1 Objectif du MCD

Le MCD permet de représenter **les entités principales du système**, leurs attributs,
ainsi que **les relations entre elles**, indépendamment de toute implémentation technique.

---

### 2.2 Description des entités

#### MEMBRE

Représente un membre du club EIC.

**Attributs principaux:**

- id_membre (identifiant)
- nom
- prenom
- email
- role (membre, chef de cellule, administrateur)

---

#### CELLULE

Représente une cellule fonctionnelle du club.

**Exemples:**

- Marketing
- Management
- Ressources Humaines

**Attributs principaux:**

- id_cellule
- nom_cellule
- description

---

#### EVENEMENT

Représente un événement organisé par le club.

**Attributs principaux:**

- id_evenement
- titre
- date_evenement
- lieu
- description

---

#### MESSAGE

Permet la communication interne entre les membres.

**Attributs principaux:**

- id_message
- contenu
- date_envoi

---

#### CONTACT

Représente un contact externe au club.

**Exemples:**

- Sponsors
- Partenaires
- Intervenants

**Attributs principaux:**

- id_contact
- nom
- email
- telephone
- type_contact

---

### 2.3 Associations et cardinalités

#### APPARTENIR

- Relation entre **MEMBRE** et **CELLULE**
- Un membre appartient à **une seule cellule**
- Une cellule peut avoir **plusieurs membres**

Cardinalité:

- MEMBRE (1,1) — CELLULE (0,n)

---

#### PARTICIPER

- Relation entre **MEMBRE** et **EVENEMENT**
- Un membre peut participer à plusieurs événements
- Un événement peut avoir plusieurs membres

Cardinalité:

- MEMBRE (0,n) — EVENEMENT (0,n)

---

#### ENVOYER/RECEVOIR

- Relation entre **MEMBRE** et **MESSAGE**
- Un message est envoyé par un seul membre
- Un membre peut envoyer et recevoir plusieurs messages

---

#### AJOUTER

- Relation entre **MEMBRE** et **CONTACT**
- Un membre peut ajouter plusieurs contacts
- Un contact est ajouté par un seul membre

---

#### GERER

- Relation entre **CELLULE** et **CONTACT**
- Une cellule peut gérer plusieurs contacts
- Un contact est géré par une seule cellule

---

## 3. Modèle Logique de Données Relationnel (MLDR)

![MLDR](MLDR.png)

### 3.1 Objectif du MLDR

Le MLDR traduit le MCD en un modèle **directement exploitable par une base de données relationnelle**.

Il définit:

- Les tables
- Les clés primaires
- Les clés étrangères
- Les types de données

---

### 3.2 Passage du MCD au MLDR

- Chaque entité devient une table
- Les associations 1,n sont traduites par des clés étrangères
- Les associations n,n sont traduites par des tables intermédiaires

---

### 3.3 Cohérence du modèle

Le MLDR respecte:

- L’intégrité référentielle
- La normalisation
- Les règles de gestion du club EIC

---

## 4. Lien avec le script SQL

Le fichier 'schema.sql' contient le script SQL permettant de:

- Créer toutes les tables
- Définir les clés primaires et étrangères
- Mettre en œuvre le MLDR dans un SGBD relationnel
