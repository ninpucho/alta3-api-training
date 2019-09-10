#!/usr/bin/env python3

import urllib.request
import json
from pprint import pprint

MAJORTOM = "http://api.open-notify.org/astros.json"


def add_astronaut(object):
    name = input("Please enter astronaut name: ")
    craft = input("Please enter craft name: ")

    if name and craft:
        object["people"].append({"name": name.title(), "craft": craft.title()})
        object["number"] += 1
    else:
        print("Name and Craft are empty...")

    return object


def main():
    groundcrtl = urllib.request.urlopen(MAJORTOM)

    helmet = groundcrtl.read()

    helmetson = json.loads(helmet.decode('utf-8'))

    print("\n\nConverted python data")
    print(helmetson)

    print('\n\nPeople in space: ', helmetson['number'])
    people = helmetson['people']
    print(people)

    while True:
        action = input("Do you wish to add another astronaut? (y/N): ")
        if action.lower() != "y":
            break
        helmetson = add_astronaut(helmetson)

    for person in people:
        print(person["name"], "is on the", person["craft"])
    print(f"Total: {helmetson['number']}")
    # Buzz Aldrin
    # mark Watney


main()