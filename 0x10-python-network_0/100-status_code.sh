#!/bin/bash
# using curl a script that sends requests and dispays only the status code
curl -s -o /dev/null -w "%{http_code}" "$1"
