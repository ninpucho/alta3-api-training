#!/usr/bin/env python3

import requests
import argparse

URL = "https://swapi.co/api/people/?format=json"


def get_data(att):
    r = requests.get(URL)
    # print(r.json())
    print(att)
    sw_info = r.json()['results']
    char_found = False
    index = -1
    idx = 0
    for x in sw_info:
        if x['name'].lower() == args.character.lower():
            sw_info = x
            char_found = True
            # idx = sw_info.index(x)
            break
        idx += 1

    if char_found:
        if args.full:
            get_full_bio(sw_info)
        else:
            for x in att:
                print(f"{sw_info['name']}'s {x} is {sw_info[x]}")
    else:
        print(f"{args.character} was not found.")

def sortLen(object):

    for key, value in sorted(object.items(), key=lambda item: len(str(item[1]))):
        print("%s: %s" % (key, value))

def get_attributes():
    r = requests.get("https://swapi.co/api/people/1/?format=json")
    print("Available attributes: ", end="")
    a = []
    a.extend(r.json().keys())
    # for x in r.json().keys():
    #     a.append(x)
    #     print(f"{x} = {r.json()[x]}")
    # print("")
    print(sorted(a, key=len))
    sortLen(r.json())

def get_full_bio(object):
    # r = requests.get(url)
    a = []
    y = []
    y.extend(object.keys())
    print(sorted(y, key=len))
    sortLen(object)
    print(f"x values = {y}")

def get_characters():
    r = requests.get(URL)
    print("Available characters: ", end="")
    for x in r.json()['results']:
        print(f"{x['name']}", end=", ")
    print("")

def main():

    if args.selection:
        get_attributes()
    elif args.all:
        get_characters()
    else:
        arg_list = args.attribute.split(",")
        get_data(arg_list)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-a", "--attribute", default="height", help="please enter an attribute, "
                                                  "you can enter multiple values as comma separated "
                                                  "-a hair_color,skin_color...")
    parser.add_argument("-c", "--character", help="Please enter a Star Wars Character's name..")
    parser.add_argument("-s", "--selection", action="store_true", help="select this option to view available options.")
    parser.add_argument("--all", action="store_true", help="List all available characters...")
    parser.add_argument("-f", "--full", action="store_true", help="Display full bio")
    args = parser.parse_args()
    main()
