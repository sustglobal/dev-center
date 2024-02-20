FROM jupyter/minimal-notebook:ubuntu-22.04

ADD . /opt/dev-center
ADD jupyter-notebooks/*.ipynb /home/jovyan/work/

USER root
RUN apt-get update --fix-missing
RUN apt-get install -y software-properties-common
RUN apt-get install -y gcc g++
RUN add-apt-repository -y ppa:ubuntugis/ppa
RUN apt update
RUN apt install -y gdal-bin libgdal-dev

USER $NB_UID
RUN pip install --user -r /opt/dev-center/jupyter-notebooks/requirements.txt

# uncomment following two lines to install sust-api-client
# package from local source
#USER root
#RUN pip install --user /opt/dev-center/clients/python

WORKDIR /home/jovyan/work