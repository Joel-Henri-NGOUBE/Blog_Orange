# Blog_Orange

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




