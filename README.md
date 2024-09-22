# Projet API - Gestion des tâches - Flask

### Description

Cette application gère une liste de tâches (CRUD) et génère des statistiques en fonction de leur statut 

### Prérequis

-Python 3
-pip
-Flask
-Flask-CORS

### Installation 

1. ** Télécharger le projet **

2. ** Installer les dépendances**

```pip install -r requirements.txt```

3. ** Lancer l'application **
```flask run```

Le serveur est disponible à l'adresse : 'http://127.0.0.1:5000'


### Routes de l'API

#### 1. Récupérer toutes les tâches
- **GET** `/tasks?offset=<offset>&limit=<limit>`

#### 2. Trouver une tâche par ID
- **GET** `/tasks/<id_tache>`

#### 3. Créer une tâche
- **POST** `/tasks`

#### 4. Modifier une tâche
- **PUT** `/tasks/<id_tache>`

### 5. Supprimer une tâche
- **DELETE** `/tasks/<id_tache>`

### 6. Statistiques sur les tâches
- **GET** `/statistics/status`
