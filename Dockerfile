FROM python:3.6.8-stretch

WORKDIR /home/user/work

RUN pip install django

EXPOSE 8000

CMD  [ "/bin/bash" ]