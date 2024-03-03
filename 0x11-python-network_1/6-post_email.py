#!/usr/bin/python3
"""
script that takes in a URL and an email address,
sends a POST request to the passed URL with the
email as a parameter,
and finally displays the body of the response.
"""

import sys
import requests


if __name__ == "__main__":
    """
    fetch the url address
    """
    url = sys.argv[1]
    emil = sys.argv[2]
    data = {'email': emil}

    # send a POST request to the URL address and displays resp
    rspns = requests.post(url, data=data)
    print(rspns.text)
