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
