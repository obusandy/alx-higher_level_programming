#!/bin/bash
# sends a JSON POST request anddisplays response must use curl
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
