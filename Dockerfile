FROM ubuntu:22.04
LABEL maintainer="Claes Nygren <claes@allwidgets.com>"

RUN apt update
RUN apt -y upgrade

RUN apt -y install software-properties-common emacs-nox git

RUN add-apt-repository ppa:deadsnakes/ppa -y

RUN apt -y install python3.10 python3-pip python3.10-venv

RUN  mkdir /runeberg_selmalagerlof

COPY ./runeberg_selmalagerlof/runeberg_selmalagerlof.py /runeberg_selmalagerlof/runeberg_selmalagerlof.py
COPY ./runeberg_selmalagerlof/joiner.py /runeberg_selmalagerlof/joiner.py
COPY ./runeberg_selmalagerlof/fancy_prepare.py /runeberg_selmalagerlof/fancy_prepare.py
COPY ./runeberg_selmalagerlof/train_selmalagerlof.py /runeberg_selmalagerlof/train_selmalagerlof.py
COPY ./runeberg_selmalagerlof/runeberg_selmalagerlof_books.json /runeberg_selmalagerlof/runeberg_selmalagerlof_books.json

WORKDIR /wrk

COPY ./handle.sh /
RUN chmod 755 /handle.sh

ENTRYPOINT ["/handle.sh"]

# cmd ["python3","/runeberg_selmalagerlof/runeberg_selmalagerlof.py"]




