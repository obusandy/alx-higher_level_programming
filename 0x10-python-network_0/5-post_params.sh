#!/bin/bash
# takes url as arg, sends post request andfinally displays the response
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
