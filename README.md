# Whitehat

⚠️ **WARNING THIS PYTHON LIBRARY FOR EDUCATIONAL PURPOSES ONLY** ⚠️

## Features
- DDoS
- More features soon!

## Install
`pip install whitehat`

## Example
- ### DDoS
```
import whitehat

ddos = whitehat.ddos_target("0.0.0.0", 80, 1200)  #IP, PORT, DURATION
whitehat.start_ddos(ddos)
```
