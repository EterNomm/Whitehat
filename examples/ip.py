import whitehat

ip = whitehat.ip("ip address")

web_ip = whitehat.ip.get_ip("example.com")
ip_location = ip.get_location()
ip_info = ip.get_info()  # already including location

print(web_ip)
print(ip_location)
print(ip_info)
