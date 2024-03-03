#!/usr/bin/python3
"""
Fetches a URL, prints the response body, and handles
errors with informative messages
- If the HTTP status code is greater than or equal to 400,
print: Error code: followed by the value of the HTTP status code
"""
import sys
import requests


if __name__ == "__main__":
    """
    entry point.
    """
    url = sys.argv[1]
    rspns = requests.get(url)

    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(rspns.text)
