import json
from urllib.request import urlopen

class ip:
    def __init__(self, ip_address):
        self.ip = ip_address

    def get_location(self):
        ip_addr = self.ip
        url = f'http://ipinfo.io/{ip_addr}/json'
        response = urlopen(url)
        data = json.load(response)

        loc=data['loc']
        print(loc)

    def get_info(self):
        ip_addr = self.ip
        url = f'http://ipinfo.io/{ip_addr}/json'
        response = urlopen(url)
        data = json.load(response)
        ip=data['ip']
        org=data['org']
        city = data['city']
        country=data['country']
        region=data['region']
        time_zone=data['timezone']
        postal=data['postal']
        loc=data['loc']
        hostname=data['hostname']
        
        print()
        print(f"IP : {ip}")
        print(f"Hostname : {hostname}")
        print(f"City : {city}")
        print(f"Region : {region}")
        print(f"Country : {country}")
        print(f"Location : {loc}")
        print(f"Organization : {org}")
        print(f"Post Code : {postal}")
        print(f"Timezone : {time_zone}")
        print()
