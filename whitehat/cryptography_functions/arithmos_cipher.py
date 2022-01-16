# I made this cipher myself. If you want to see the repository, you can look at https://github.com/LyQuid12/arithmos-cipher

from .dictionary import *
from ..errors import *
import re

class ArithmosCipher_function:
    def __init__(self):
        pass

    @classmethod
    def encrypt(self, text:str=None):
        if text == None:
            raise CannotNone("text")
        return ''.join(encrypt_dict[c] for c in list(text))

    @classmethod
    def decrypt(self, cipher:int=None):
        if cipher == None:
            raise CannotNone("cipher")
        cipher = str(cipher)
        split_num = re.findall("\d{2}|\w|.|\d\s|\s+|\d$", cipher)
        decrypted = ''.join(decrypt_dict[c] for c in split_num)
        return decrypted
