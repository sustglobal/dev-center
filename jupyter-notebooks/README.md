# Sust Global Dev Center Jupyter Notebooks

If you are looking for information regarding usage of these Jupyter notebooks, please start with the published
documentation at 
https://developers.sustglobal.com/jupyter-notebooks.html.

## Local Development

If you need to build the docker image yourself, start by cloning the dev-center repo locally:

```
git clone git@github.com:sustglobal/dev-center.git
```

Build the docker image with the following command, which must be executed from the root of the dev-center git repository:

```
docker build -f jupyter-notebooks/Dockerfile . -t sustglobal-dev-center-jupyter-notebooks
```

After the image has been built, you can return to the public documentation and simply use your custom image in
place of the published image.

You may also want to mount the local jupyter-notebooks directory into the container as a volume.
The following is an example docker command that may help (execute this from the root of the dev-center repo):

```
docker run -e SUST_API_KEY="YOUR-API-KEY" -v $(pwd)/jupyter-notebooks:/home/jovyan/work -p 8888:8888 -it sustglobal-dev-center-jupyter-notebooks
```
