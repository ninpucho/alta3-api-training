#!/usr/bin/env python3
import time
import urllib.request
import re
from datetime import datetime


def get_external_ip():
    url = 'http://checkip.dyndns.org'
    requesty = urllib.request.urlopen(url).read().decode('utf-8')
    print(requesty)
    # requesty = "<html><head><title>Current IP Check</title></head><body>Current IP Address: 70.198.93</body></html>"
    externalIP = re.findall(r'(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})', requesty)
    print(externalIP)
    # print(f'{y=time.process_time()}')
    if externalIP:
        valid = valid_ip(externalIP[0])
        return valid
    return {'valid': False, 'value': ''}


def valid_ip(ip_tuple):
    output = {'valid': True, 'value': ''}
    output['valid'] = True
    for x in ip_tuple:
        if int(x) <0 or int(x) > 255:
            output['valid'] = False

    if valid_ip:
        output['value'] = ".".join(ip_tuple)

    return output




def processed(dt_start, process):
    lap = datetime.now() - dt_start
    print(f'{process} completed in {lap}')
    return datetime.now()

lap = processed(datetime.now(), "import")

print(get_external_ip())
lap = processed(lap, "import")

regex = {}
regex['name'] = '[a-zA-Z0-9]+'
regex['safe_char'] = '[^";:,]'
regex['qsafe_char'] = '[^"]'
lap = processed(lap, "import")

# the value of a parameter will either just be regular characters, ie
# safe_char or it will be quoted in case we only accepting inside
# doublequotes (") or escaped doublequotes (\")
regex['param_value'] = r"""(?:"|\\") %(qsafe_char)s * (?:"|\\") | %(safe_char)s + """ % regex
regex['param'] = r""" (?: %(name)s ) = (?: %(param_value)s )? """ % regex

print(regex['param'])

print(time.process_time())
lap = processed(lap, "import")
