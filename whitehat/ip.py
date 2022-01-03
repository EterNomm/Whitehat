import json
from typing import Dict, Any
from urllib.request import urlopen
import socket
from .errors import *

class IP:
    r"""A class that implements IP function
    -----------
    Parameters :
    - IP: :class:`str` | Set IP
    """

    def __init__(self, IP:str):
        invalid_ip = ["https://", "http://"]

        if any(v in IP for v in invalid_ip):
            raise InvalidIP

        self.ip = IP
        res=urlopen(f'http://ipinfo.io/{self.ip}/json')
        self.res = json.load(res)

    @property
    def location(self) -> str:
        return self.res.get('loc')

    @property
    def org(self) -> str:
        return self.res.get('org')

    @property
    def city(self) -> str:
        return self.res.get('city')

    @property
    def country(self) -> str:
        return self.res.get('country')

    @property
    def region(self) -> str:
        return self.res.get('region')

    @property
    def timezone(self) -> str:
        return self.res.get('timezone')

    @property
    def postal(self) -> str:
        return self.res.get('postal')

    @property
    def hostname(self) -> str:
        return self.res.get('hostname')


    def get_all_info(self, format:str):
        r"""
        A method to get all IP info
        -----
        Parameters :
        - format: `str` | list or json
        """

        if format == "list":
            data = f"\nIP : {self.ip}\nHostname : {self.hostname}\nCity : {self.city}\nRegion : {self.region}\nCountry : {self.country}\nLocation : {self.location}\nOrganization : {self.org}\nPost Code : {self.postal}\nTimezone : {self.timezone}\n"
        elif format == "json":
            data = {"ip" : {self.ip}, "hostname" : self.hostname, "city" : self.city, "region" : self.region, "country" : self.country, "location" : self.location, "organization" : self.org, "post code" : self.postal, "timezone" : self.timezone}
        else:
            raise InvalidFormat
        
        return data

    @classmethod
    def get_ip(self, url:str):
        r"""
        A method to get IP by URL/web address
        -----
        Parameters :
        - url: `str` | Target URL. Cannot include : https:// and http://
        """
        invalid_url = ["https://", "http://"]

        if any(v in url for v in invalid_url):
            raise InvalidURL

        ip = socket.gethostbyname(url)
        return ip
