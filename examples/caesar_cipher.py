import whitehat

# Encrypt
encrypted = whitehat.Cryptography.CaesarCipher.encrypt(text="LyQuid", shift=12)
print(encrypted)

# Decrypt
decrypted = whitehat.Cryptography.CaesarCipher.decrypt(cipher=encrypted, shift=12)
print(decrypted)
