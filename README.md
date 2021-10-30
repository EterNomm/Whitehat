[![PyPI - Downloads](https://img.shields.io/pypi/dm/whitehat?color=white&label=Downloads&logo=python)](https://pypi.org/project/whitehat)
[![PyPI](https://img.shields.io/pypi/v/whitehat?label=PyPI%20Version&logo=pypi)](https://pypi.org/project/whitehat)
[![Discord](https://img.shields.io/discord/887650006977347594?color=blue&label=EterNomm&logo=discord)](https://discord.com/invite/qpT2AeYZRN)
[![Discord](https://img.shields.io/discord/835863428450877441?color=blue&label=NekoIceTeam&logo=discord)](https://discord.com/invite/hNtA2uEb7J)

# Whitehat

⚠️ **WARNING THIS PYTHON LIBRARY FOR EDUCATIONAL PURPOSES ONLY** ⚠️

## Features
- DDoS (Can up to 1000 Requests per seconds)
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
