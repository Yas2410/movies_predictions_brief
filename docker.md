# Création Dockerfile

```docker
FROM python:3.11

COPY . /src

WORKDIR /src

RUN pip install -r requirements.txt

EXPOSE 5000
 
CMD ["python", "app.py"]
```

# Lignes de commandes docker

`docker build -t yaslud:latest .`

`docker run -p 5000:5000 yaslud:latest`

# Déploiement dans Azure

- Créer un repo dans Docker Hub (https://hub.docker.com/)  
    => J'ai appelé mon repo luddrt/yaslud

- Reconstruire l'imae pour pouvoir l'envoyer dans le repo :  
    `docker build -t luddrt/yaslud:latest .`  
    `docker push luddrt/yaslud:latest`

- Dans Azure :
    - Créer une Web app
    - Choisir le mode de publication "Conteneur"
    - Lier l'image précédemment exportée sur Docker Hub
