#!/bin/bash
# a Bash script that takes in a URL,sends and displays
curl -s "$1" | wc -c
