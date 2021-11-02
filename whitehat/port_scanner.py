import socket

def port_scan(IP:str, PORT:int):
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(10)

    def scan(PORT):
        if s.connect_ex((IP, PORT)):
            log_close = f"Port {PORT} is Closed"
            return log_close
        else:
            log_open = f"Port {PORT} is Open"
            return log_open

    return scan(PORT)
