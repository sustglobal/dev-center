#!/bin/bash -e

rm -fr clients/python/sust/api/generated

mkdir -p clients/tools/cache
cachefile="clients/tools/cache/climate-explorer-openapi-spec.json"

ENDPOINT=${ENDPOINT:-"https://explorer.sustglobal.io"}

wget $ENDPOINT/swagger.json -O $cachefile
echo $(jq '.host="explorer.sustglobal.io"' $cachefile) > $cachefile

docker run --rm \
    -v $PWD:/dev-center openapitools/openapi-generator-cli generate \
    -i /dev-center/clients/tools/cache/climate-explorer-openapi-spec.json \
    -g python \
    -o /dev-center/clients/python \
    -c /dev-center/clients/tools/openapi-clientgen-config-python.json \
    --skip-validate-spec

# This file always gets deleted by the generator, so we return
# it to its former glory for convenience
git checkout clients/python/sust/api/__init__.py
