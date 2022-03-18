# I made this cipher myself. If you want to see the repository, you can look at https://github.com/LyQuid12/arithmos-cipher

import arithmos
from ..errors import *

class ArithmosCipher_function:
    def __init__(self):
        pass

    @classmethod
    def encrypt(self, text:str):
        if text == None:
            raise CannotNone("text")
        else:
            return arithmos.encrypt(text)

    @classmethod
    def decrypt(self, cipher:str):
        if cipher == None:
            raise CannotNone("cipher")
        else:
            return arithmos.decrypt(cipher)
