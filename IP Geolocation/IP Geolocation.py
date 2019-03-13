"""
    This code allows you to geo locate your IP address.
"""

import urllib.request as ureq
import json

url = "https://extreme-ip-lookup.com/json"

ip_inf = json.load(ureq.urlopen(url))

print("IP Geolocation Info:\n")
for param, val in ip_inf.items():
    print(f"{param.upper()}{' ' * (15 - len(param))}: {val if len(val) != 0 else 'NA'}")
