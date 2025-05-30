# Projet Base de Données - Gestion d'Hôtels

# Description

Interface web de gestion d'hôtels développée avec Streamlit et SQLite pour le projet de Bases de Données (Projet 

réalisé dans le cadre du cours de Bases de Données Pr. J.ZAHIR - Licence IAP S4 2025).

# Fonctionnalités

📋 Consulter la liste des réservations

👥 Consulter la liste des clients

🏨 Consulter les chambres disponibles par période

➕ Ajouter un nouveau client

📅 Ajouter une nouvelle réservation

# Structure du Projet
```bash
├── app.py              # Interface Streamlit principale
├── database.py         # Gestion de la base de données SQLite
├── requirements.txt    # Dépendances Python
├── README.md          # Documentation
└── hotel.db           # Base de données SQLite (générée automatiquement)
```

# Installation et Lancement

Prérequis

Python 3.7+

pip

# Installation

# Cloner le repository

```bash
git clone <votre-repo-url>
cd projet-bd-hotel
```

# Installer les dépendances

```bash 
pip install -r requirements.txt
```

# Lancer l'application
```bash
streamlit run app.py
```

L'application sera accessible à l'adresse : 
``` http://localhost:8501 ```

# Base de Données 

Modèle Conceptuel

La base de données comprend les tables suivantes :

Hotel : Informations sur les hôtels

Client : Données clients

Prestation : Services proposés

TypeChambre : Types de chambres disponibles

Chambre : Détails des chambres

Reservation : Réservations effectuées

Evaluation : Évaluations des clients

# Initialisation Automatique

Au premier lancement, la base de données est automatiquement créée et peuplée avec les données fournies dans le sujet.

# Utilisation

*Consultation des Réservations*

Affiche toutes les réservations avec les détails client et hôtel

*Informations* : ID, dates, client, hôtel, ville

*Gestion des Clients*

Liste complète des clients enregistrés

Possibilité d'ajouter de nouveaux clients

*Champs :* nom, email, téléphone, adresse

*Disponibilité des Chambres*

Recherche par période (date début/fin)

Affichage des chambres libres avec détails

Filtrage par type de chambre

*Nouvelles Réservations*

Sélection du client et de la chambre

Choix des dates de séjour

Validation automatique de la disponibilité

# Technologies Utilisées

Python 3.x : Langage principal

Streamlit : Framework web

SQLite : Base de données

Pandas : Manipulation des données

# Auteurs

MOUKOUCH Adam IAP S4 Gr4

ALOUAH Abdelkrim IAP S4 Gr2 
