**Description**
This project is a test for ayomi based on Django 
**How to launch application**
 - pull the project from github : 
  `git pull https://github.com/daktap/AyomiProject.git`
 - build docker image using dockerfile dans le dossier du projet lance la commande:
  `docker build -t ayomi .`
 - run docker container based on created image et enjoy sur http://127.0.0.1:8000/
 - `docker run -p 8000:8000 ayomi`

