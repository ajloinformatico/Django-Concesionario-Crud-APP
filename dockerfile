FROM python:3.7
RUN apt-get update
RUN apt-get -y upgrade
RUN apt -y install nano
RUN pip install Django
RUN pip install mysqlclient
