#!/usr/bin/python3
"""
The below script
takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter,
and displays the body of the response
(decoded in utf-8)
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    eml = {"email": sys.argv[2]}
    addrs = urllib.parse.urlencode(eml).encode("ascii")

    reqst = urllib.request.Request(url, addrs)
    with urllib.request.urlopen(reqst) as rspe:
        print(rspe.read().decode("utf-8"))
