FROM node:latest

RUN apt-get update && apt-get -y install python3 python3-venv python-is-python3

RUN git clone https://github.com/cbenning/fussel.git && cd fussel && ./setup.sh

COPY config.yml fussel/config.yml