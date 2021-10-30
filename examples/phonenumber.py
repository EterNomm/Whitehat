import whitehat

number = whitehat.phonenumber.set_number("phone_number") # Don't forget to use Country Code. Ex : +62 / +1
whitehat.phonenumber.timezone(number)
whitehat.phonenumber.carrier(number)
whitehat.phonenumber.region(number)
whitehat.phonenumber.is_valid(number)
