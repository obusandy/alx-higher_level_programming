#!/usr/bin/python3
"""
Fetches a specified URL, extracts the X-Request-Id header value,
and prints it. takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable
"""
if __name__ == "__main__":
    import urllib.request as rec
    from sys import argv
    riq = rec.Request(argv[1])
    with rec.urlopen(riq) as rst:
        print(rst.headers.get('X-Request-Id'))
