---
title: Jupyter Notebooks
---

The [Jupyter notebooks](http://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html) contained in this repo are from the software developers, data scientists, and developer advocates at [Sust Global](https://www.sustglobal.com/). These interactive, open-source ([Apache 2.0 license](https://github.com/sustglobal/dev-center/blob/main/LICENSE)) guides are designed to help you explore Planet data, work with our APIs and tools, and learn how to extract insights from our climate scenario analysis datasets.


## Using the Notebooks

It is recommended that you start from the published docker image, which contains everything needed to run a Jupyter
notebook server locally with all of the Developer Center notebooks.

The following command will first download the published image, then execute a server locally.
Please note that `SUST_API_KEY` must be set to your own Climate Explorer API key:

```
docker run -e SUST_API_KEY="YOUR-API-KEY" -p 8888:8888 --pull=always -it us-central1-docker.pkg.dev/sust-dev-03/sustglobal-dev-center/jupyter-notebooks
```

If the command above is successful, you will be presented with a set of links to a local server.
Click on the link that looks like `http://localhost:8888/?token=XYZ` (typically the last link printed to the terminal).

Now from your browser you should choose a notebook to start.
A good place to begin is `ClimateExplorerAPIDemo.ipynb`, which is a quick demonstration of the python API client.
Note the commentary in the first cell requiring further input from you.

To stop the server, simply `ctrl+C` and confirm.

## Local Development

Please see the [documentation on Github](https://github.com/sustglobal/dev-center/blob/master/jupyter-notebooks/README.md) if you desire to work with local assets.
