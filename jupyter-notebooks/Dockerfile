FROM jupyter/minimal-notebook

ADD . /opt/dev-center
ADD jupyter-notebooks/*.ipynb /home/jovyan/work

RUN pip install --user -r /opt/dev-center/jupyter-notebooks/requirements.txt

USER root
RUN pip install --user /opt/dev-center/clients/python

WORKDIR /home/jovyan/work
