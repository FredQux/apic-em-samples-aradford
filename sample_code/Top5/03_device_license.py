#!/usr/bin/env python
from __future__ import print_function
import sys
from util import get_url
import json


def ip_to_id(ip):
    return get_url("network-device/ip-address/%s" % ip)['response']['id']

def get_interfaces(id):
    return get_url("license-info/network-device/%s" % id)

def print_licence(licences):
    print("{name:16}{status:9}{type:20}{maxUsageCount}".
          format(name="Name",
                 status="Status",
                 type="Type",
                 maxUsageCount="maxUsageCount"))

    for licence in licences['response']:
        maxusage = "N/A" if 'maxUsageCount' not in licence else licence['maxUsageCount']

        print("{name:16}{status:9}{type:20}{maxUsageCount}".
              format(name=licence['name'],
                     status=licence['status'],
                     type=licence['type'],
                     maxUsageCount=maxusage))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        dev_id = ip_to_id(sys.argv[1])
        licences = get_interfaces(dev_id)
        print_licence(licences)
        #print(json.dumps(licences, indent=2))

    else:
        print("Usage: %s device_ip", sys.argv[0])