class binary_function:
    def __init__(self):
        pass

    @classmethod
    def encrypt(self, text):
        binary = " ".join(format(ord(i), 'b') for i in text)
        return binary

    @classmethod
    def decrypt(self, binary):
        text_string = "".join([chr(int(binary, 2)) for binary in binary.split(" ")])
        return text_string
