#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8).
-have to manage urllib.error.HTTPError exceptions and print:
-Error code: followed by the HTTP status code
"""
import sys
import urllib.error
import urllib.request
if __name__ == "__main__":
    address = sys.argv[1]
    rqst = urllib.request.Request(address)
    try:
        with urllib.request.urlopen(rqst) as rspons:
            print(rspons.read().decode("ascii"))
    except urllib.error.HTTPError as errr:
        print("Error code: {}".format(errr.code))
