# Projet 11 OpenClassRoom : Améliorez une application Web Python par des tests et du débogage
## Présentation du projet
Le but de ce projet est de corriger des bugs et de terminer un prototype de plateforme numérique pour
coordonner les compétitions de force.
Il faut également rajouter des tests pour voir si les bugs ont été corrigés et si il n'y a pas d'autres bugd.
On rajoutera également des tests de performance.

## composition
Tous les fichiers .py necessaires au fonctionnement du logiciel se trouvent dans le répertoire src.
Les autres fichiers sont :
- README.md qui contient des informations sur le logiciel
- requirements.txt contient les packages necessaires au bon fonctionnement du logiciel
- tox.ini permet de paramétrer flake8 pour voir si le programme répond aux normes pep8

## Installation de l'application
- Cloner le dépôt de code à l'aide de la commande `https://github.com/Jean-PierreBE/Gudlft.git`
- Rendez-vous depuis un terminal à la racine du répertoire SoftDesk avec la commande `cd Gudlft`
- Créer un environnement virtuel pour le projet avec `$ python -m venv env` sous windows ou `$ python3 -m venv env` sous macos ou linux.
- Activez l'environnement virtuel avec `$ env\Scripts\activate` sous windows ou `$ source env/bin/activate` sous macos ou linux.
- installer les packages python du fichier requirements.txt en lançant la commande suivante 
  - `pip install -r requirements.txt`

les packages installés sont les suivants :
- click
- Flask
- itsdangerous
- Jinja2
- MarkupSafe
- Werkzeug
- pytest
- locust

## Lancement du programme
- On lance le programme en tapant sur la ligne de commande dans le répertoire src:
  - `python server.py`

## Déroulement du programme
Une fois la commande précédente exécutée, mettre l'adresse suivante
- `http://127.0.0.1:5000/`
dans le browser de votre choix.
- un écran d'accueil apparaît permettant à un utilisateur de se connecter 
- sur cet écran d'accueil l'utilisateur pourra également afficher un dashboard contenant le nombre de points par club
- une fois connecté l'utilisateur voit son nombre de points disponibles et la liste des compétitions avec le nombre de place
- l'utilisateur pourra choisir une compétition et réserver un certain nombre de places compte tenu de :
  - un point donne droit à une place
  - le nombre de places maximum de réservation est de 12

## Tests
pour voir si le programme passe les tests unitaires et d'intégration exécuter la commande suivante :
- `pytest --html=test_report.html --self-contained-html`
- visualiser le fichier test_report.html
pour voir la couverture des tests lancer la commande suivante :
- `pytest --cov=. --cov-report html`
- visualiser le fichier index.html dans le répertoire htmlcov
pour faire des tests de performance
- aller dans le répertoire tests
- lancer la commande suivante :
  - `locust -f test_performance.py --html=performance_report.html`
  - aller sur l'url `http://localhost:8089/`
    - choisir le nombre d'utilisateur , 
    - l'url à tester `http://127.0.0.1:5000/`
    - stopper l'exécution sur l'url
    - stopper le serveur
- visualiser le rapport performance_report.html

## Contrôle qualité
Pour vérifier la qualité du code , on peut lancer la commande suivante :
- `flake8 --format=html --htmldir=flake-report src`
Le rapport sortira en format html dans le répertoire flake-report

pour cela il faut installer :
- flake8 : contrôle du code pour vérifier la compatibilité avec les normes pep8
- flake8-html : permet de sortir le rapport flake8 sous format html
- flake8-functions : permet d'ajouter des contrôles au niveau des fonctions (ex : longueur maximale des fonctions)

le fichier tox.ini contient la configuration pour flake8.
- `exclude = venv` : ne contrôle pas la directory venv
- `max-line-length = 120` : la longueur maximale de chaque ligne ne peut pas dépasser 120 caractères
- `max-function-length = 50` : la longueur maximale de chaque fonction ne peut pas dépasser 50 lignes
- `ignore = CFQ002, CFQ004, W503, W504` : évite les erreurs
  - CFQ002 : nombre d'arguments en entrée trop élevés (> 6)
  - CFQ004 : nombre d'éléments en retour trop élevés (> 3)
  - W503 : saut de ligne avant un opérateur
  - W504 : saut de ligne après un opérateur

Ces paramètres peuvent être modifiés
