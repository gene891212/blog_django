FROM python:3.6.8-stretch

WORKDIR /work

COPY ./requirements.txt .
RUN pip install -r requirements.txt

ENV DJANGO_SECRET_KEY="YOUR_SECRET_KEY"
EXPOSE 8000

CMD  [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]