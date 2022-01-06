import whitehat

# Encrypt
encrypted = whitehat.CaesarCipher.encrypt(text="LyQuid", shift=12)
print(encrypted)

# Decrypt
decrypted = whitehat.CaesarCipher.decrypt(cipher="XkCgup", shift=12)
print(decrypted)
