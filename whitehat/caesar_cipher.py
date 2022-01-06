import string
from .errors import *

class CaesarCipher:
    r"""A class that implements Caesar Cipher encryption
    -----------
    Classmethod :
    - encrypt
    - decrypt
    """

    def __init__(self):
        pass

    @classmethod
    def encrypt(self, text:str=None, shift:int=2):
        r"""A method that implements encrypting strings to Caesar Cipher encryption
        -----------
        Parameters :
        - text: `str` | Set string to encrypt
        - shift: `int` | Set encryption shift. Cannot exceed 25 (Default : 2)
        """

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
    def decrypt(self, cipher:str=None, shift:int=2):
        r"""A method that implements Caesar Cipher decryption to string
        -----------
        Parameters :
        - cipher: `str` | Set Caesar Cipher string to decrypt
        - shift: `int` | Set encryption shift. Cannot exceed 25 (Default : 2)
        """

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
