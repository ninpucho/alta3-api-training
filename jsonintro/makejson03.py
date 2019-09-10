#!/usr/bin/env python3

import json


def main():
    with open("datacenter.json", "r") as datacenter:
        datacenterstring = datacenter.read()

    print(datacenterstring)
    print(type(datacenterstring))
    print("\nThe code above is string data python cannot wasily work with this data")
    input("Please press enter")

    datacenterdecoded = json.loads(datacenterstring)

    print(type(datacenterdecoded))

    print(datacenterdecoded)

    print(datacenterdecoded["row3"])
    print(datacenterdecoded["row2"][1])

    print(datacenterdecoded["row3"][-1])

main()