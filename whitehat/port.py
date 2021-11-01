import socket

class port:
    def __init__(self, IP, PORT):
        self.IP = IP
        self.PORT = PORT

    def scan(self):
        IP = self.IP
        PORT = self.PORT
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(10)
    
        def scan(PORT):
            if s.connect_ex((IP, PORT)):
                print(f"Port {PORT} is Closed")
            else:
                print(f"Port {PORT} is Open")
    
        scan(PORT)
