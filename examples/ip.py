import whitehat

ip = whitehat.IP("IP")
ip = ip.get_all_info(format="list") # list/json
print(ip)

web = whitehat.IP.get_ip("github.com")
print(web)
