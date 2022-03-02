FROM jupyter/minimal-notebook:2022-02-22

ADD . /opt/dev-center
ADD jupyter-notebooks/*.ipynb /home/jovyan/work

RUN pip install --user -r /opt/dev-center/jupyter-notebooks/requirements.txt

# uncomment following two lines to install sust-api-client
# package from local source
USER root
RUN pip install --user /opt/dev-center/clients/python

WORKDIR /home/jovyan/work
