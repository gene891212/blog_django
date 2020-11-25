FROM python:3.6.8-stretch

WORKDIR /work

RUN pip install django
ENV DJANGO_SECRET_KEY=
EXPOSE 8000

CMD  [ "/bin/bash" ]