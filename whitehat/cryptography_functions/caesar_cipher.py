import string
from ..errors import *

class CaesarCipher_function:

    def __init__(self):
        pass

    @classmethod
    def encrypt(self, text, shift):
        if text == None:
            raise CannotNone("text")
        if shift >= 26:
            raise ShiftExceededTheLimit
        
        alphabets = [string.ascii_lowercase, string.ascii_uppercase, string.punctuation]

        def shift_alphabet(alphabets):
            return alphabets[shift:] + alphabets[:shift]

        shifted_alphabets = tuple(map(shift_alphabet, alphabets))
        final_alphabet = ''.join(alphabets)
        final_shifted_alphabet = ''.join(shifted_alphabets)

        table = str.maketrans(final_alphabet, final_shifted_alphabet)
        
        return text.translate(table)

    @classmethod
    def decrypt(self, cipher, shift):
        if cipher == None:
            raise CannotNone("cipher")
        if shift >= 26:
            raise ShiftExceededTheLimit

        alphabets = [string.ascii_lowercase, string.ascii_uppercase, string.punctuation]

        shift = 26-shift

        def shift_alphabet(alphabets):
            return alphabets[shift:] + alphabets[:shift]

        shifted_alphabets = tuple(map(shift_alphabet, alphabets))
        final_alphabet = ''.join(alphabets)
        final_shifted_alphabet = ''.join(shifted_alphabets)

        table = str.maketrans(final_alphabet, final_shifted_alphabet)

        return cipher.translate(table)
