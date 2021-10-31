import whitehat

pn = whitehat.phonenumber("phone_number") # Don't forget to use Country Code. Ex : +62 / +1

pn.timezone()
pn.carrier()
pn.region()
pn.is_valid()

# to get all information
pn.get_all_info()
