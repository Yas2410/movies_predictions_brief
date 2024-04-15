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

# Déploiement dans Azure (Web app)

- Créer un repo dans Docker Hub (https://hub.docker.com/)  
    => J'ai appelé mon repo luddrt/yaslud

- Reconstruire l'image pour pouvoir l'envoyer dans le repo :  
    `docker build -t luddrt/yaslud:latest .`  
    `docker push luddrt/yaslud:latest`

- Dans Azure :
    - Créer une Web app : `app-docker-p5`
    - Choisir le mode de publication "Conteneur"
    - Lier l'image précédemment exportée sur Docker Hub

- Dans un navigateur internet :  
https://app-docker-p5.azurewebsites.net/

# Publication de l'image dans un registre de conteneurs Azure

Avec Azure CLI :  
Connexion azure : `az login`  
Connexion au registre : `az acr login --name registryludo`  
Alias de l'image à publier : `docker tag yaslud registryludo.azurecr.io/projets/yaslud`  
Publication : `docker push registryludo.azurecr.io/projets/yaslud`  

# Déploiement dans Azure (Container instance)

Dans Azure Cloud Shell (bash) :  
Génération d'un DNS unique : `DNS_NAME_LABEL=aci-ludo-$RANDOM`  
Création du conteneur avec l'image Docker Hub :  
`az container create --resource-group rg-Ludo --name container-ludo --image index.docker.io/luddrt/yaslud:latest --ports 5000 --dns-name-label $DNS_NAME_LABEL --location westeurope`  
Création du conteneur avec l'image Azure Conteneur Registry :  
`az container create --resource-group rg-Ludo --name container-ludo2 --image registryludo.azurecr.io/projets/yaslud --ports 5000 --dns-name-label $DNS_NAME_LABEL --location westeurope`

Dans un navigateur internet :  
http://aci-ludo-1016.westeurope.azurecontainer.io:5000/

Second lien : 
http://movieprediction-yasludo.francecentral.azurecontainer.io:5000/

NB : L'adresse générée lors du déploiement ne mentionne pas le port.
Ne pas oublier de l'ajouter à la fin de l'url