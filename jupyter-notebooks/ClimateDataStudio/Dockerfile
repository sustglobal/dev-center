FROM ubuntu:20.04

RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \
    python3-pip \
    jq \
    libgdal-dev \
    gdal-bin
WORKDIR /app
COPY . .
RUN pip install rasterio==1.2.10
RUN pip3 install -r requirements.txt
# docker run -v $PWD:/app -p 8888:8888 -it dev-center jupyter notebook --ip 0.0.0.0 --no-browser --allow-root
