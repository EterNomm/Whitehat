import socket

def get_ip(website: str):
    ip_addr = socket.gethostbyname(website)
    ip_addr = f"{website}   :   {ip_addr}"
    return ip_addr
