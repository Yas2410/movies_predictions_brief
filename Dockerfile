FROM python:3.11

COPY ./models/ /src/models
COPY ./static/ /src/static
COPY ./templates/ /src/templates
COPY ./app.py /src
COPY ./requirements.txt /src

WORKDIR /src

RUN pip install -r requirements.txt

EXPOSE 5000
 
CMD ["python", "app.py"]
