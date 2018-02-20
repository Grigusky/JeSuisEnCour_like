Back, partie django
===================

### en local sur ton pc


Procédure pour lancer le back de la copie de je suis en cour:

dans un premier temps installer python (version 3):
https://www.python.org/downloads/

dans un second merci de l’ajouter dans vos variables d’environnement

Par la suite merci de créer un environnement virtuel dans le but d’éviter tous conflits avec le système

    -    pip install --user virtualenv
    -    python -m venv /path/vers/projet/env_nom_du_projet
    -    lancer le Script/activate.bat

si tu veux en savoir plus:
http://sametmax.com/les-environnement-virtuels-python-virtualenv-et-virtualenvwrapper/

par la suite il faut télécharger les modules pour le projet dans l’env, nous allons placer par le requirements.txt, ce qui va nous donner:

    -    pip install -r requirements.txt

Pour lancer le serveur, je t’invite à te diriger dans la directory ou est présente le fichier manage.py, par la suite tu peux lancer la commande suivante:
    
    -     python manage.py runserver # si tu veux mettre sur une ip et un port #

si tu veux lancer des migrations, tu fais un :
    
    -     python manage.py makemigrations && python manage.py migrate

### en direct sur le serveur

le projet sur le serveur tourne directement en instance docker.

si tu veux le lancer je t'invite à effectuer les actions disponnible dans la partie suivante



Back, partie scripté
====================

pour la partie scripté du projet il vous suffit de lancer le script main.