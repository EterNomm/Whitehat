import whitehat

port = whitehat.Port(IP="127.0.0.1", PORT=80)
print(port.scan())
