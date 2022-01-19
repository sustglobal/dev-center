#!/bin/bash

rm -r clients/python/sust/api/generated

mkdir -p clients/tools/cache
wget https://explorer.sustglobal.io/swagger.json -O clients/tools/cache/climate-explorer-openapi-spec.json

docker run --rm \
    -v $PWD:/dev-center openapitools/openapi-generator-cli generate \
    -i /dev-center/clients/tools/cache/climate-explorer-openapi-spec.json \
    -g python \
    -o /dev-center/clients/python \
    -c /dev-center/clients/tools/openapi-clientgen-config-python.json \
    --skip-validate-spec
