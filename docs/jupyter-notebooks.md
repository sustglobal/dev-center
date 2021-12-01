---
layout: default
title: Jupyter Notebooks
---

The [Jupyter notebooks](http://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html) contained in this repo are from the software developers, data scientists, and developer advocates at [Sust Global](https://www.sustglobal.com/). These interactive, open-source ([MIT 2021 License](https://github.com/sustglobal/dev-center/blob/main/LICENSE)) guides are designed to help you explore Planet data, work with our APIs and tools, and learn how to extract insights from our climate scenario analysis datasets.

## System Requirements

* [Python 3](https://www.python.org/downloads/release/python-380/)

## Clone or update repo:

If you've never cloned the Sust Global dev-center repo, run the following:

```bash
git clone https://github.com/sustglobal/dev-center.git
cd jupyter-notebooks
```

## Set Up

Install the python dependencies needed to run our Jupyter notebooks:

```bash
virtualenv -p python3 venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## Run a Notebook

Start up a Jupyter notebook server:

```bash
jupyter notebook
```
