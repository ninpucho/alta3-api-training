#!/usr/bin/env python3
"""ALTA3 Research | Authother ......"""
import requests


LOOKUPAPI = "http://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=172042&date=2019-01-21&distance=25&API_KEY=B2281235-B907-4E91-98F1-59B1A4E6927A"


def main():
    r = requests.get(LOOKUPAPI)

    print(dir(r))

main()
