#!/usr/bin/python3
"""
Fetches a custom URL, prints information about the response
fetches https://alx-intranet.hbtn.io/status
must use a with statementi
"""
if __name__ == "__main__":
    import urllib.request as request
    with request.urlopen('https://alx-intranet.hbtn.io/status') as rs:
        rspns = rs.read()
        print('Body response:')
        print("\t- type: {}".format(type(rspns)))
        print("\t- content: {}".format(rspns))
        print("\t- utf8 content: {}".format(rspns.decode('utf-8')))
