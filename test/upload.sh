#!/bin/bash

###
# Simple upload test to Flow' docker image
# $FILE is defined through env variable in CI's job"
###

curl -X GET -o $FILE -s "http://docker:8000/getfile/10"
response=$(curl -X POST -o /dev/null -s -w "%{http_code}\n" -F "file=@$FILE" "http://docker:8000/putfile")

if [[ "$response" != "200" ]]; then
    echo "Upload failed with HTTP return code $response"
    exit 1
fi
