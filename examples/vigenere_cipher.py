import whitehat

# Encrypt
encrypt = whitehat.Cryptography.VigenereCipher.encrypt("LyQuid", "EterNomm")
print(encrypt)

# Decrypt
decrypt = whitehat.Cryptography.VigenereCipher.decrypt("PRULVR", "EterNomm")
print(decrypt)
