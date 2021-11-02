import phonenumbers
from typing import Optional, Tuple, Dict, Any
from phonenumbers import carrier, geocoder, timezone

class phonenumber:
    def __init__(self, phone_number: str):
        self.phone_number = phonenumbers.parse(phone_number)
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

    def get_all_info(self) -> Dict[str, Any]:
        data={'timezone': self.timezone, "provider": self.provider, "region": self.region, "is_valid": self.is_valid()}
        return data
