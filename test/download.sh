#!/bin/bash

###
# Simple download test to Flows' docker image
# $FILE is defined through env variable in CI's job"
###

response=$(curl -X GET -o $FILE -s -w "%{http_code}\n" "http://docker:8000/getfile/10")

if [[ "$response" != "200" ]]; then
    echo "Download failed with HTTP return code $response"
    exit 1
fi
