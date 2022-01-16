import requests as req

encrypt_url = "https://raw.githubusercontent.com/LyQuid12/arithmos-dictionary/master/encrypt.json"
decrypt_url = "https://raw.githubusercontent.com/LyQuid12/arithmos-dictionary/master/decrypt.json"

encrypt = req.get(encrypt_url)
encrypt_dict = encrypt.json()

decrypt = req.get(decrypt_url)
decrypt_dict = decrypt.json()
