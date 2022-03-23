#!/bin/bash -ex
#
# NOTE: this script should be run from the root of the dev-center repository

TAG=sustglobal-dev-center-sphinx

docker build -f ./clients/python/sphinx/Dockerfile . -t $TAG
docker run -v $(pwd):/workspace $TAG sphinx-build -c /workspace/clients/python/sphinx -b html /workspace/clients/python/sphinx/src /workspace/docs/py
