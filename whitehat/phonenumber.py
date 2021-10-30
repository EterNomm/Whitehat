import phonenumbers
from phonenumbers import carrier, geocoder, timezone

class phonenumber:
    def set_number(phone_number):
        global the_number
        the_number = phonenumbers.parse(phone_number)
        print(the_number)

    def timezone(phone_number):
        tz = timezone.time_zones_for_number(the_number)
        print(tz)

    def carrier(phone_number):
        provider = carrier.name_for_number(the_number, "en")
        print(provider)

    def region(phone_number):
        region = geocoder.description_for_number(the_number, "en")
        print(region)
