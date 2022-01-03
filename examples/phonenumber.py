import whitehat

pn = whitehat.Phonenumber("+1234567890") # Don't forget to use Country Code. Ex : +62 / +1

print(pn.timezone)
print(pn.carrier)
print(pn.region)
print(pn.is_valid())

# to get all information
print(pn.get_all_info(format="json")) # Format : "json", "list"
