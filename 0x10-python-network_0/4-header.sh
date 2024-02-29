#!/bin/bash
# this is a script that takes in a url as an arg
# sends a GET request to the URL, and displays the body of the response
curl -sH "X-School-User-Id: 98" "$1"
