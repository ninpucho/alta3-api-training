#!/usr/bin/env python3

import requests
import argparse
from pprint import pprint

def main():
    mytoken = '6f7c07868655762c3f4ef76d41de9b394f2f876e967ab4a4'
    myapi = f'https://fonoapi.freshpixl.com/v1/{args.action.lower()}'
    brand = ''
    device = ''
    mybuiltapi = myapi + "?token=" + mytoken
    print(mybuiltapi)
    # myjson = requests.get(mybuiltapi).json()

    # for x in myjson:
    #     print(x)

    print("=" * 70)
    # brand = input("What brand of device are you serarching for? " )
    print(args)
    if args.brand:
        brand = "&brand=" + args.brand
    if args.device:
        device = "&device=" + args.device

    myjson = requests.get(mybuiltapi + brand + device).json()
    # print(myjson["message"])
    for x in myjson:
        pprint(x)



if __name__ == '__main__':

    parse = argparse.ArgumentParser()
    parse.add_argument("action", help="enter getdevice or getbrand", default="getlatest" )
    parse.add_argument("-b", "--brand", help="Enter a brand to search for..")
    parse.add_argument("-d", "--device", help="Enter device to use..")
    args = parse.parse_args()

    main()