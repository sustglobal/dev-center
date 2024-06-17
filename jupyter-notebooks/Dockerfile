FROM jupyter/minimal-notebook:ubuntu-22.04

USER root
RUN apt-get update --fix-missing
RUN apt-get install -y software-properties-common
RUN apt-get install -y gcc g++
RUN add-apt-repository -y ppa:ubuntugis/ppa
RUN apt update
RUN apt install -y gdal-bin libgdal-dev

USER $NB_UID

ADD jupyter-notebooks/requirements.txt /opt/dev-center/jupyter-notebooks/requirements.txt
RUN pip install --user -r /opt/dev-center/jupyter-notebooks/requirements.txt

ADD jupyter-notebooks/*.ipynb /home/jovyan/work/

# uncomment following two lines to install sust-api-client
# package from local source
#USER root
#RUN pip install --user /opt/dev-center/clients/python

WORKDIR /home/jovyan/work