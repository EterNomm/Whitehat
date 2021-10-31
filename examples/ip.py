import whitehat

ip = whitehat.ip("ip address")

ip_location = ip.get_location()
ip_info = ip.get_info()  # already including location

print(ip_location)
print(ip_info)
