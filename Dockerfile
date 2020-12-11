FROM python:3.6.8-stretch

WORKDIR /work

COPY ./requirements.txt .
RUN pip install -r requirements.txt

ENV DJANGO_SECRET_KEY="wym$$m@h$7v%k7#ys#tdr^u!a!p+wh=f&5v98c*t$d$lp2^hh4"
EXPOSE 8000

CMD  [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]