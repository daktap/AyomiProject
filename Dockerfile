FROM ubuntu:18.04
USER root
EXPOSE 8000
RUN apt-get -y update 
RUN apt-get -y install build-essential checkinstall
RUN apt install -y  python2.7 python-pip
RUN pip install Django==1.8
RUN useradd -ms /bin/bash hassen
USER hassen
COPY . /home/hassen/mysite
WORKDIR /home/hassen/mysite
CMD python manage.py runserver 0.0.0.0:8000
