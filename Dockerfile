FROM python:3.8-alpine

ENV FLASK_APP 441D_filme
#ENV FLASK_CONFIG = docker

#3.8 booster
#RUN useradd -rm -d /home/site -s /bin/bash -g root -G sudo -u 1001 site

#3.8 alpine
RUN adduser -D 441D_filme

USER 441D_filme

WORKDIR /home/mariusdaniel99/Desktop/Proiect/curs_vcgj_441D_filme

COPY app app
#COPY dockerstart.sh dockerstart.sh

RUN python -m venv .venv
RUN .venv/bin/pip install -r app/quickrequirements.txt

WORKDIR /home/mariusdaniel99/Desktop/Proiect/curs_vcgj_441D_filme/app

# runtime configuration
EXPOSE 5011
ENTRYPOINT ["./dockerstart.sh"]
#CMD flask run --host 0.0.0.0 -p 5010
