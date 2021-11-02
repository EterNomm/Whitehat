import whitehat
from whitehat.utilities import get_ip

ip = whitehat.ip("ip address")

web_ip = get_ip("example.com")
ip_location = ip.location
ip_info = ip.get_all_info("format")  # already including location. Format : "json", "list"

print(web_ip)
print(ip_location)
print(ip_info)
