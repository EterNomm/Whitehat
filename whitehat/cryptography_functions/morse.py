MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

class morse_function:
    def __init__(self):
        pass

    @classmethod
    def encrypt(self, text:str):
        text = text.upper()
        cipher = ''
        for letter in text:
            if letter != ' ':
                cipher += MORSE_CODE_DICT[letter] + ' '
            else:
                cipher += ' '
            
        return cipher

    @classmethod
    def decrypt(self, morse:str):
        morse += ' '
        decipher = ''
        citext = ''
        for letter in morse:
            if (letter != ' '):
                i = 0
                citext += letter
            else:
                i += 1
                if i == 2 :
                    decipher += ' '
                else:
                    decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                    citext = ''
                    
        return decipher
