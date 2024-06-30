# Blog_Orange

Bonjour monsieur/madame.

J'espère que vous vous portez bien.

J'ai réalisé le test que vous m'avez proposé de faire par rapport à votre offre d'alternance Développeur Backend Django.

Ci-après se trouvent respectivement les liens vers le dépôt GitHub ainsi que le lien du domaine du site hébergé avec Render.

https://github.com/Joel-Henri-NGOUBE/Blog_Orange

https://blog-orange-u862.onrender.com/fr/blog

J'ai quelques mots à ajouter par rapport à l'élaboration du projet.

J'ai commencé le projet assez tard parce que j'avais un projet de fin d'année réalisé sous-forme d'un hackathon la semaine passée et cette semaine j'étais en stage donc je n'avançais que le soir.

En ce qui concerne la fonctionnalité optionnelle du LLM, le modèle le moins lourd de GPT4 n'est pas compatible avec l'environnement de déploiement (vous vous en rendrez compte en testant) et les autres étant trop lourds ne peuvent pas être installés sur le serveur de Render avec la version gratuite.

Cependant j'ai beaucoup appris de la programmation avec Django et de l'internationalisation 🥲 et c'était un projet intéressant à réaliser.

Comme points d'amélioration du projet, je noterais:

- Rendre l'application responsive
- Améliorer le typage des variables (notamment au niveau des objets spécifiques à Django)
- Ajouter une section de préférences pour définir par exemple la langue par défaut pour les prochaines connexions
- Enregistrer dans la base de données les questions et les réponses des utilisateurs connectés

## Configuration

- Cloner le dépôt en faisant `git clone https://github.com/Joel-Henri-NGOUBE/Blog_Orange.git`

- Créer un environnement virtuel dans le projet pour éviter d'installer les dépendances en global avec la commande `python -m venv .venv`

- Se déplacer dans l'environnement virtuel en faisant `./.venv/Scripts/Activate.ps1` sur Windows avec Powershell ou `source ./.venv/bin/activate` sur Linux ou MacOS.

- Au besoin, il existe un superuser dont les identifiants sont `jojo` et `jojo`
  
## Installation

- Exécuter la commande `pip install -r requirements.txt` (Pas nécessaire avec Docker)

## Lancement

### En local 

- Exécuter la commande `gunicorn multilang_site.wsgi --bind=0.0.0.0:8000` (ou `gunicorn multilang_site.wsgi`) -- Sur Windows il peut y avoir une incompatibilité avec gunicorn à cause du module `fcntl`

- Vous pouvez accéder au site en accédant à l'adresse `http://localhost:8000`
  
### En local avec Docker

- Créer une image Docker avec la commande `docker image build -t orange:v1 .`

- Créer le container qui permettra de servir les fichiers de l'application avec `docker run --name orange -d -p 8080:8000 orange:v1`

- Vous pouvez accéder au site en accédant à l'adresse `http://localhost:8080` 

- Vous pouvez également interagir avec l'environnement d'exécution de docker en faisant `docker exec -ti orange bash`

<!-- ### En local avec Docker Compose

- Réaliser l'entièreté des commandes précédentes avec la commande `docker compose -d up`

- Vous pouvez accéder au site en accédant à l'adresse `http://localhost:8080` -->




