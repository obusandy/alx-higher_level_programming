#!/usr/bin/python3
"""
 a Python script that takes in a letter and sends a POST request
 to http://0.0.0.0:5000/search_user with the letter as a parameter.
 - letter must be sent in the variable q
 - response body is properly JSON formatted and not empty,
 - display the id and name like this: [<id>] <name>
"""
import sys
import requests


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}

    res = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        rspns = res.json()
        if rspns == {}:
            print("No result")
        else:
            print("[{}] {}".format(rspns.get("id"), rspns.get("name")))
    except ValueError:
        print("Not a valid JSON")
