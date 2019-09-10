#!/usr/bin/env python3

import json


def main():
    hitchhikers = [{"name": "Zaphod Beeblebrox", "species": "Betelgeusian"},
                  {"name": "Arthur Dent", "species": "Human"}]

    print(hitchhikers)

    zfile = open("galaxyguide.json", "w")

    json.dump(hitchhikers, zfile)
    jsonstring = json.dumps(hitchhikers)

    print(jsonstring)
    zfile.close()


main()

