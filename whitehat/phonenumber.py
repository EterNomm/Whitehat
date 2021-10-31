import phonenumbers
from phonenumbers import carrier, geocoder, timezone

class phonenumber:
    def __init__(self, phone_number):
        pn = phonenumbers.parse(phone_number)
        self.phone_number = pn
        print()
        print(pn)

    def timezone(self):
        phone_number = self.phone_number
        tz = timezone.time_zones_for_number(phone_number)
        print(f"Timezone : {tz}")

    def carrier(self):
        phone_number = self.phone_number
        provider = carrier.name_for_number(phone_number, "en")
        print(f"Carrier : {provider}")

    def region(self):
        phone_number = self.phone_number
        region = geocoder.description_for_number(phone_number, "en")
        print(f"Region : {region}")

    def is_valid(self):
        phone_number = self.phone_number
        is_valid = phonenumbers.is_valid_number(phone_number)
        print(f"Is Valid Phone Number : {is_valid}")

    def get_all_info(self):
        phone_number = self.phone_number
        tz = timezone.time_zones_for_number(phone_number)
        provider = carrier.name_for_number(phone_number, "en")
        region = geocoder.description_for_number(phone_number, "en")
        is_valid = phonenumbers.is_valid_number(phone_number)
        print(f"Timezone : {tz}")
        print(f"Carrier : {provider}")
        print(f"Region : {region}")
        print(f"Is Valid Phone Number : {is_valid}")
        print()
