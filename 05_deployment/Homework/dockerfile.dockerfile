FROM python:3.8.12-slim

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["app.py", "model1.bin", "./"]

EXPOSE 9696

ENTRYPOINT ["waitress-serve", "port=9696","url-scheme=http://localhost:9696/predict", "app:app"]