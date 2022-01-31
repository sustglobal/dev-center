---
title: Jupyter Notebooks
---

The [Jupyter notebooks](http://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html) contained in this repo are from the software developers, data scientists, and developer advocates at [Sust Global](https://www.sustglobal.com/). These interactive, open-source ([Apache 2.0 license](https://github.com/sustglobal/dev-center/blob/main/LICENSE)) guides are designed to help you explore Planet data, work with our APIs and tools, and learn how to extract insights from our climate scenario analysis datasets.


## Using the Notebooks

The quickest way to get started here is to use the included Dockerfile to run a local Jupyter notebook server.
Start by cloning the git repository into a local directory:

```
git clone git@github.com:sustglobal/dev-center.git
```

Build the docker image with the following command, which must be executed from the root of the dev-center git repository:

```
docker build -f jupyter-notebooks/Dockerfile . -t sust-dev-center-notebooks
```

After the image has been built, you may start the server with the following command.
Please note that `SUST_API_KEY` must be set to your own Climate Explorer API key:

```
docker run -e SUST_API_KEY="YOUR-API-KEY" -v $(pwd):/home/jovyan/work -p 8888:8888 -it sust-dev-center-notebooks
```

If the command above is successful, you will be presented with a set of links to a local server.
Click on the link that looks like `http://localhost:8888/?token=XYZ` (typically the last link printed to the terminal).

Now from your browser you should choose a notebook to start.
A good place to begin is `ClimateExplorerAPIDemo.ipynb`, which is a quick demonstration of the python API client.
Note the commentary in the first cell requiring further input from you.

To stop the server, simply `ctrl+C` and confirm.
