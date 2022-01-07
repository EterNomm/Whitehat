import whitehat

# Encrypt
encrypted = whitehat.Cryptography.Morse.encrypt("lyquid")
print(encrypted)

# Decrypt
decrypted = whitehat.Cryptography.Morse.decrypt(encrypted)
print(decrypted)
