# Using These Notebooks

## Prereqs
First, copy any relevant data into the ./data folder. For the purposes of the USCitiesExample, this would include USCities.csv, and USA_2.geojson.

Next, run the developer center docker image (execute this from the root of the dev-center repo):

```bash
docker run -v $(pwd)/jupyter-notebooks:/home/jovyan/work -p 8888:8888 -it us-central1-docker.pkg.dev/sust-dev-03/sustglobal-dev-center/jupyter-notebooks
```

## Examples

You should see in your terminal something like `http://127.0.0.1:8888/lab?token=xyz`, copy that link into your browser.

Open up `SegmentedDatasetsAnalysis` and find the example you want to use!