#!/usr/bin/env python3

import argparse
import time
import hashlib
import requests
from pprint import pprint

base_url = 'http://gateway.marvel.com/v1/public/characters'

def hasgbuilder(timeywimey, pvkee, pubkee):
    return hashlib.md5((timeywimey+pvkee+pubkee).encode('utf-8')).hexdigest()

def marvelcharcall(stampystamp, hashyhash, pkeyz, myargs):

    my_params = {
        "comics": "",
        "name": "",
        "series": "",
        "events": "",
        "stories": ""
    }
    url = f"{base_url}?ts={stampystamp}&apikey={pkeyz}&hash={hashyhash}"

    for i in my_params:
        if args.__getattribute__(i) != None:
            url += f"&{i}={args.__getattribute__(i)}"
    print(url)
    r = requests.get(url)

    return r.json()

def main():
    with open(args.dev) as mccoy:
        beast = mccoy.read().rstrip('\n')

    with open(args.pub) as munrow:
        storm = munrow.read().rstrip('\n')

    nightcrawler = str(time.time()).rstrip('.') #.replace('.', "")

    print(nightcrawler, beast, storm, sep="\n")
    cerebro = hasgbuilder(nightcrawler, beast, storm)

    uncannyxmen = marvelcharcall(nightcrawler, cerebro, storm, args)

    # pprint(uncannyxmen)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--dev', help='help provide path to dev key')
    parser.add_argument('--pub', help='provide path to public key')
    parser.add_argument('-n', '--name', help='provide a character name')
    parser.add_argument('--comics', help='provide a comic')
    parser.add_argument('--series', help='provide a series')
    parser.add_argument('--events', help='provide an even')
    parser.add_argument('--stories', help='provide a story')
    args = parser.parse_args()
    print(args)
    print(args.__getattribute__("name"))
    main()