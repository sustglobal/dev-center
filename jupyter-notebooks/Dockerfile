FROM jupyter/minimal-notebook

ADD jupyter-notebooks/requirements.txt /tmp/dev-center/jupyter-notebooks/requirements.txt
RUN pip install --user -r /tmp/dev-center/jupyter-notebooks/requirements.txt

ADD clients/python /opt/dev-center/clients/python
USER root
RUN pip install --user /opt/dev-center/clients/python

WORKDIR /home/jovyan/work/jupyter-notebooks
