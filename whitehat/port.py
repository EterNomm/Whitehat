import socket
from .errors import *


class Port:
    r"""A class that implements Port function
    -----------
    Parameters :
    - IP: :class:`str` | Set  IP
    - PORT: :class:`int` | Set PORT
    """

    def __init__(self, IP:str, PORT:int):
        invalid_ip = ["https://", "http://"]
    
        if any(v in IP for v in invalid_ip):
            raise InvalidIP
        
        self.IP = IP
        self.PORT = PORT


    def scan(self):
        r"""
        Scan IP and PORT
        """
        IP = self.IP
        PORT = self.PORT
    
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(10)
    
        def scan(PORT):
            if s.connect_ex((IP, PORT)):
                log_close = f"{IP}:{PORT} is Closed"
                return log_close
            else:
                log_open = f"{IP}:{PORT} is Open"
                return log_open
    
        return scan(PORT)
