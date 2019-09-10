#!/usr/bin/env python3

import urllib.request
import json

MAJORTOM = "http://api.open-notify.org/astros.json"


def main():
    groundcrtl = urllib.request.urlopen(MAJORTOM)

    helmet = groundcrtl.read()


    helmetson = json.loads(helmet.decode('utf-8'))


    print("\n\nConverted python data")
    print(helmetson)


    print('\n\nPeople in space: ', helmetson['number'])
    people = helmetson['people']
    print(people)

    for person in people:
        print(person["name"], "is on the", person["craft"])

main()