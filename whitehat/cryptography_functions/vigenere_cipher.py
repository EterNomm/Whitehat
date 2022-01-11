def generate_key(string, key):
    string = str.upper(string)
    key = str.upper(key)
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) -
					len(key)):
                    key.append(key[i % len(key)])
        return("" . join(key))



class vigenerecipher_function:
    def __init__(self) -> None:
        pass

    @classmethod
    def encrypt(self, text:str, key:str):
        string = str.upper(text)
        key = str.upper(key)
        key = generate_key(text, key)
        cipher_text = []
        for i in range(len(string)):
            x = (ord(string[i]) + ord(key[i])) % 26
            x += ord('A')
            cipher_text.append(chr(x))
        return("" . join(cipher_text))

    @classmethod
    def decrypt(self, cipher:str, key:str):
        orig_text = []
        key = generate_key(cipher, key)
        for i in range(len(cipher)):
            x = (ord(cipher[i]) -
	    		ord(key[i]) + 26) % 26
            x += ord('A')
            orig_text.append(chr(x))
        return("" . join(orig_text))
