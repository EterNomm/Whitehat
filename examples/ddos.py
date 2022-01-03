import whitehat

ddos = whitehat.DDoS(IP="IP", PORT=80, duration=120)
ddos.start()
