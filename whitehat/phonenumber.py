import phonenumbers
from typing import Optional, Tuple, Dict, Any
from phonenumbers import carrier, geocoder, timezone

from .errors import *

class Phonenumber:
    r"""A class that implements Keylogger function
    -----------
    Paramaters :
    - phonenumber: `str` | Set phonenumber (Must include country code)
    """

    def __init__(self, phonenumber: str):
        self.phone_number = phonenumbers.parse(phonenumber)
        self.provider = self.carrier #An alias to self.carrier
        
    @property
    def timezone(self) -> Optional[Tuple[str]]:
        tz = timezone.time_zones_for_number(self.phone_number)
        return tz

    @property
    def carrier(self) -> str:
        provider = carrier.name_for_number(self.phone_number, "en")
        return provider

    @property
    def region(self) -> str:
        region = geocoder.description_for_number(self.phone_number, "en")
        return region

    def is_valid(self) -> bool:
        is_valid = phonenumbers.is_valid_number(self.phone_number)
        return is_valid

    def get_all_info(self, format:str) -> Dict[str, Any]:
        r"""
        Get all phonenumber information
        -----
        Paramater :
        - format: `str` | list/json
        """
        if format == "json":
            data={'timezone': self.timezone, "provider": self.provider, "region": self.region, "is_valid": self.is_valid()}
        elif format == "list":
            data=f"Timezone : {self.timezone}\nProvider : {self.provider}\nRegion : {self.region}\nIs Valid : {self.is_valid()}"

        else:
            raise InvalidFormat

        return data
