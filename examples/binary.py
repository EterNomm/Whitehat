import whitehat

# Encrypt
encrypted = whitehat.Cryptography.Binary.encrypt("LyQuid")
print(encrypted)

# Decrypt
decrypted = whitehat.Cryptography.Binary.decrypt(encrypted)
print(decrypted)
