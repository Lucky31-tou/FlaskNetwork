# Application Web avec Flask et SQLite

Ceci est une application web simple développée avec le micro-framework Python Flask. Elle permet de gérer des utilisateurs (inscription, connexion, mise à jour, suppression) et de créer des publications associées à chaque utilisateur. La persistance des données est assurée par une base de données SQLite.

## Fonctionnalités

- **Gestion des Utilisateurs** :
  - Création de nouveaux comptes utilisateurs avec un mot de passe haché.
  - Connexion des utilisateurs existants.
  - Page de compte personnalisée pour chaque utilisateur.
  - Mise à jour du nom d'utilisateur.
  - Suppression d'un compte utilisateur.
- **Gestion des Publications** :
  - Ajout de publications (titre et corps de texte) par un utilisateur connecté.
  - Affichage de toutes les publications sur la page de compte de l'utilisateur.
- **Base de Données** :
  - Utilisation de SQLite pour une configuration légère.
  - Commande CLI personnalisée (`flask init-db`) pour initialiser la base de données.

## Prérequis

Avant de commencer, assurez-vous d'avoir installé les éléments suivants sur votre machine :
- Python 3.8+
- pip (généralement inclus avec Python)

## Installation et Lancement

Suivez ces étapes pour mettre en place et lancer l'application localement.

1.  **Clonez le dépôt** (si vous utilisez git) ou assurez-vous d'avoir les fichiers du projet.

2.  **Créez un environnement virtuel** (recommandé) :
    ```bash
    python -m venv venv
    ```

3.  **Activez l'environnement virtuel** :
    - Sur Windows :
      ```bash
      .\venv\Scripts\activate
      ```
    - Sur macOS/Linux :
      ```bash
      source venv/bin/activate
      ```

4.  **Installez les dépendances** :
    Créez un fichier `requirements.txt` avec le contenu suivant :
    ```
    Flask
    Werkzeug
    click
    ```
    Puis installez-les :
    ```bash
    pip install -r requirements.txt
    ```

5.  **Configurez l'application Flask** :
    Définissez la variable d'environnement `FLASK_APP`.
    - Sur Windows (Command Prompt) :
      ```bash
      set FLASK_APP=sql.app
      ```
    - Sur Windows (PowerShell) :
      ```powershell
      $env:FLASK_APP = "sql.app"
      ```
    - Sur macOS/Linux :
      ```bash
      export FLASK_APP=sql.app
      ```

6.  **Initialisez la base de données** :
    Cette commande exécute le script `schema.sql` pour créer les tables `user` et `post`.
    ```bash
    flask init-db
    ```
    Un fichier `db.sqlite` sera créé à la racine du projet.

7.  **Lancez l'application** :
    ```bash
    flask run
    ```

L'application sera accessible à l'adresse http://127.0.0.1:5000.

## Structure du Projet

```
module_flask/
├── sql/
│   ├── __init__.py
│   ├── app.py          # Logique de l'application Flask (routes, vues)
│   ├── db.py           # Fonctions pour la gestion de la base de données
│   └── schema.sql      # Schéma SQL pour la création des tables
├── templates/
│   ├── index.html      # Page d'accueil
│   ├── add.html        # Formulaire d'inscription
│   ├── login.html      # Formulaire de connexion
│   ├── account.html    # Page de compte utilisateur
│   └── update.html     # Formulaire de mise à jour
└── README.md           # Ce fichier
```

Auteur : Louis DUBOIS
