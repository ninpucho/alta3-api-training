#!/usr/bin/env python3

import sys

ARGS = sys.argv



def parse_args(object):

    new_args = {
        "Username": {
            "options": ["-u", "--username"],
            "help": "Please enter a username...",
        },
        "Password": {
            "options": ["-p", "--password"],
            "help": "Please enter a password..."
        },
        "Ip Address": {
            "options": ["-i", "--ip"],
            "help": "Please enter a ip address..."
        },
        "Gateway": {
            "options": ["-g", "--gateway"],
            "help": "Please enter a username..."
        },
    }





params = {
    "username": "",
    "password": "",
    "ipaddress": "",
    "gateway": "",
}

if len(args) > 1:
    for i in args:
        i = i.split("=", 1)
        if len(i) > 1:
            print(i[0], "==", i[1])
            field = i[0]
            value = i[1]
            params[field] = value
        else:
            print("single", i[0])

print(params)