from .cryptography_method.caesar_cipher import *
from .cryptography_method.morse import *
from .cryptography_method.binary import *

class Cryptography:

    def __init__(self):
        pass

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
            return CaesarCipher.encrypt(text=text, shift=shift)

        @classmethod
        def decrypt(self, cipher:str=None, shift:int=2):
            r"""A method that implements Caesar Cipher decryption to string
            -----------
            Parameters :
            - cipher: `str` | Set Caesar Cipher string to decrypt
            - shift: `int` | Set encryption shift. Cannot exceed 25 (Default : 2)
            """
            return CaesarCipher.decrypt(cipher=cipher, shift=shift)

    class Morse:
        r"""A class that implements Morse code encryption
        -----------
        Classmethod :
        - encrypt
        - decrypt
        """
        def __init__(self):
            pass

        @classmethod
        def encrypt(self, text:str):
            r"""A method that implements encrypting strings to Morse code
            -----------
            Parameters :
            - text: `str` | Set string to encrypt
            """
            return morse_method.encrypt(text)

        @classmethod
        def decrypt(self, morse:str):
            r"""A method that implements Morse code decryption to string
            -----------
            Parameters :
            - morse: `str` | Set Morse code string to decrypt
            """
            return morse_method.decrypt(morse)

    
    class Binary:
        r"""A class that implements Binary code encryption
        -----------
        Classmethod :
        - encrypt
        - decrypt
        """
        def __init__(self):
            pass

        @classmethod
        def encrypt(self, text:str):
            r"""A method that implements encrypting strings to Binary code
            -----------
            Parameters :
            - text: `str` | Set string to encrypt
            """

            return binary_method.encrypt(text)

        @classmethod
        def decrypt(self, binary:str):
            r"""A method that implements Binary code decryption to string
            -----------
            Parameters :
            - binary: `str` | Set Binary code string to decrypt
            """

            return binary_method.decrypt(binary)
