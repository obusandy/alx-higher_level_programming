#!/usr/bin/python3
"""
A Python script that fetches https://alx-intranet.hbtn.io/status
- must use the package requests
- not allowed to import packages other than requests
- body of the response must be display like the following
example (tabulation before -)
"""

import requests

if __name__ == "__main__":
    rs = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(rs.text)))
    print("\t- content: {}".format(rs.text))
