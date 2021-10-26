# blog_djanog
## Usage
- Pipenv
1. Download Pipenv
```sh
pip install pipenv
```

2. Build environment
```sh
pipenv sync
```

Add environment variable, you can go to [Djecrety](https://djecrety.ir) get a secret key
```sh
touch .env
echo 'DJANGO_SECRET_KEY=YOUR_SECRET_KEY' > .env
```

3. Run django server
```sh
pipenv run python manage.py makemigrations
pipenv run python manage.py migrate
pipenv run python manage.py runserver 0.0.0.0:8001
```

4. View site in your browser

Entering `http://localhost:8001` in your local browser

- Docker

1. Download Docker
2. Edit Dockerfile

Go to [Djecrety](https://djecrety.ir) get a secret key, and paste the secret key to DockerFile
```docker
FROM python:3.6.8-stretch

WORKDIR /work

COPY ./requirements.txt .
RUN pip install -r requirements.txt

ENV DJANGO_SECRET_KEY="YOUR_SECRET_KEY"
EXPOSE 8000

CMD  [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
```

3. Build environment
```sh
cd blog_django
bash build_env
```

4. View site in your browser

Entering `http://localhost:8001` in your local browser
