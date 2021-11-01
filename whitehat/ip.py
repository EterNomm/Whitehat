import json
from urllib.request import urlopen
import socket

class ip:
    def __init__(self, ip_address):
        self.ip = ip_address

    def get_ip(website):
        ip_addr = socket.gethostbyname(website)
        ip_addr = f"{website}   :   {ip_addr}"
        return ip_addr

    def get_location(self):
        ip_addr = self.ip
        url = f'http://ipinfo.io/{ip_addr}/json'
        response = urlopen(url)
        data = json.load(response)

        loc=data['loc']
        return loc

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

        all_info = f"\nIP : {ip}\nHostname : {hostname}\nCity : {city}\nRegion : {region}\nCountry : {country}\nLocation : {loc}\nOrganization : {org}\nPost Code : {postal}\nTimezone : {time_zone}\n"
        return all_info
