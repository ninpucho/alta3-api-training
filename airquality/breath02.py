#!/usr/bin/env python3
r"""ALTA3 Research | Author ......"""
import requests
from pprint import pprint
import re


LOOKUPAPI = "B2281235-B907-4E91-98F1-59B1A4E6927A"


def main():

    settings = {"zip": "17042", "date": "2019-01-21", "distance": "25"}
    while True:
        print("\nPlease enter your information:")
        print("-" * 75)
        settings["zip"] = input(f"Please enter your 5 digit zipcode [{settings['zip']}]: ")
        settings["date"] = input(f"Please enter the date you wish to view (yyyy-mm-dd) [{settings['date']}]: ")
        settings["distance"] = input(f"Please enter the distance [{settings['distance']}]: ")

        print(settings)
        if not settings["zip"] or not settings["date"] or not settings["distance"]:
            print("\nAll fields need to be populated....")
            continue


        url = f"https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode={settings['zip']}&date={settings['date']}&distance={settings['distance']}&API_KEY={LOOKUPAPI}"
        print(url)
        r = requests.get(url)
        print(r.json())
        print(f'Weather Forcast for {settings["zip"]} within {settings["distance"]} on {settings["date"]}')
        print("=" * 70)
        for x in r.json():
            print(x.get("DateForecast"))
            print("-" * 70)
            print(x.get("Discussion"))
            if x.get("ActionDay"):
                print("!!!!!WARNING!!!!!")
                print("Please stay indoors....")

        action = input("\nDo you wish to lookup another date? (Y/n) :")

        if action.lower() == "n":
            break

main()
