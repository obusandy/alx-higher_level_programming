#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and
displays the value of the variable X-Request-Id
in the response header
- must use the packages requests and sys
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    rsp = requests.get(url)
    print(rsp.headers.get("X-Request-Id"))
