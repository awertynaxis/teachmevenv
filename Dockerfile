FROM python:3.8

ENV DEBIAN_FRONTEND=noninterective
RUN apt-get upgrade
RUN apt-get -y upgrade
RUN apt-get -y install libpq-dev
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/*

ADD weddev /opt/weddev
COPY requirements.txt /opt/weddev/requirements.txt
COPY PostgresSQL_DB.py /opt/weddev/PostgresSQL_DB.py
COPY .env /opt/weddev/.env
WORKDIR /opt/weddev

RUN pip install -r requirements.txt --no-cache-dir
EXPOSE 5000

ENTRYPOINT ["./flask_like_axe.py"]