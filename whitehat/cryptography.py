from .cryptography_functions.caesar_cipher import *
from .cryptography_functions.morse import *
from .cryptography_functions.binary import *
from .cryptography_functions.vigenere_cipher import *

class Cryptography:
    r"""A core class that implements common Cryptography
    -----------
    Class :
    - CaesarCipher
    - VigenereCipher
    - Morse
    - Binary
    """
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
            return CaesarCipher_function.encrypt(text=text, shift=shift)

        @classmethod
        def decrypt(self, cipher:str=None, shift:int=2):
            r"""A method that implements Caesar Cipher decryption to string
            -----------
            Parameters :
            - cipher: `str` | Set Caesar Cipher string to decrypt
            - shift: `int` | Set encryption shift. Cannot exceed 25 (Default : 2)
            """
            return CaesarCipher_function.decrypt(cipher=cipher, shift=shift)

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
            return morse_function.encrypt(text)

        @classmethod
        def decrypt(self, morse:str):
            r"""A method that implements Morse code decryption to string
            -----------
            Parameters :
            - morse: `str` | Set Morse code string to decrypt
            """
            return morse_function.decrypt(morse)

    
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

            return binary_function.encrypt(text)

        @classmethod
        def decrypt(self, binary:str):
            r"""A method that implements Binary code decryption to string
            -----------
            Parameters :
            - binary: `str` | Set Binary code string to decrypt
            """

            return binary_function.decrypt(binary)

    class VigenereCipher:
        r"""A class that implements VigenereCipher encryption
        -----------
        Classmethod :
        - encrypt
        - decrypt
        """
        def __init__(self):
            pass

        @classmethod
        def encrypt(self, text:str, key:str):
            r"""A method that implements encrypting strings to Vigenere Cipher encryption
            -----------
            Parameters :
            - text: `str` | Set string to encrypt
            - key: `str` | Set key encryption
            """

            return vigenerecipher_function.encrypt(text, key)

        @classmethod
        def decrypt(self, cipher:str, key:str):
            r"""A method that implements Vigenere Cipher decryption to string
            -----------
            Parameters :
            - cipher: `str` | Set Vigenere Cipher string to decrypt
            - key: `str | Set key encryption
            """

            return vigenerecipher_function.decrypt(cipher, key)
