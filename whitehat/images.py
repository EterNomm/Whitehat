from .errors import *

end_hex = b"\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42\x60\x82"

class PNG:
    """
    Function for PNG.
    -
    -----
    Parameter :
    - image_path: `str` | Set PNG file to modify
    -----
    Methods :
    - hide_message
    - hide_program
    - reveal_message
    - reveal_program
    """
    def __init__(self, image_path:str=None):
        if image_path == None:
            raise CannotNone("image_path")
            
        self.image_path = image_path

    def hide_message(self, message:str=None):
        """
        Method to hide message in PNG file.
        -----
        Parameter :
        - message: `str` | Messages that want to hide
        """

        if message == None:
            raise CannotNone("message")

        encoded_msg = str.encode(message)

        with open(self.image_path, 'ab') as f:
            f.write(encoded_msg)
        print("Success!")



    def hide_program(self, program_path:str=None):
        """
        Method to hide program (`.exe`) in PNG file.
        -----
        Parameter :
        - program_path: `str` | Program that want to hide
        """

        if program_path == None:
            raise CannotNone("program_path")
        
        if ".exe" in program_path:
            pass
        else:
            program_path = program_path + ".exe"
        
        with open(self.image_path, 'ab') as f, open(program_path, 'rb') as p:
            f.write(p.read())

        print("Success!")

    
    def reveal_message(self, encoding:str="UTF-8"):
        """
        Method to reveal secret message in PNG file.
        -----
        Parameter :
        - encoding: `str` | Default: `UTF-8`
        """

        with open(self.image_path, 'rb') as f:
            content = f.read()
            offset = content.index(end_hex)
            f.seek(offset + len(end_hex))
            return f.read().decode(encoding)
    
    def reveal_program(self, new_name:str=None):
        """
        Method to reveal secret program and create new file (`.exe`) from inside PNG file.
        -
        Parameter :
        - new_name: `str` | Set name for files from PNG
        """

        if new_name == None:
            raise CannotNone("new_name")
        
        if ".exe" in new_name:
            pass
        else:
            new_name = new_name + ".exe"

        with open(self.image_path, 'rb') as f:
            content = f.read()
            offset = content.index(end_hex)
            f.seek(offset + len(end_hex))
            new_name = str(new_name)

            with open(new_name, 'wb') as p:
                p.write(f.read())
                
        print("Success!")



class JPG:
    """
    Function for JPG/JPEG.
    -
    -----
    Parameter :
    - image_path: `str` | Set PNG file to modify
    -----
    Methods :
    - hide_message
    - hide_program
    - reveal_message
    - reveal_program
    """

    def __init__(self, image_path:str=None):
        if image_path == None:
            raise CannotNone("image_path")
        self.image_path = image_path

    def hide_message(self, message:str=None):
        """
        Method to hide message in JPG/JPEG file.
        -----
        Parameter :
        - message: `str` | Messages that want to hide
        """

        if message == None:
            raise CannotNone("message")

        encoded_msg = str.encode(message)

        with open(self.image_path, 'ab') as f:
            f.write(encoded_msg)
        print("Success!")


    def hide_program(self, program_path:str=None):
        """
        Method to hide program (`.exe`) in JPG/JPEG file.
        -----
        Parameter :
        - program_path: `str` | Program that want to hide
        """

        if program_path == None:
            raise CannotNone("program_path")
        
        if ".exe" in program_path:
            pass
        else:
            program_path = program_path + ".exe"
        
        with open(self.image_path, 'ab') as f, open(program_path, 'rb') as p:
            f.write(p.read())
        print("Success!")

    
    def reveal_message(self, encoding:str="UTF-8"):
        """
        Method to reveal secret message in JPG/JPEG file.
        -----
        Parameter :
        - encoding: `str` | Default: `UTF-8`
        """

        with open(self.image_path, 'rb') as f:
            content = f.read()
            offset = content.index(bytes.fromhex('FFD9'))
            f.seek(offset + 2)

            return f.read().decode(encoding)
    
    def reveal_program(self, new_name:str=None):
        """
        Method to reveal secret program and create new file (`.exe`) from inside JPG/JPEG file.
        -
        Parameter :
        - new_name: `str` | Set name for files from JPG/JPEG
        """

        if new_name == None:
            raise CannotNone("new_name")
        
        if ".exe" in new_name:
            pass
        else:
            new_name = new_name + ".exe"

        with open(self.image_path, 'rb') as f:
            content = f.read()
            offset = content.index(bytes.fromhex('FFD9'))
            f.seek(offset + 2)
            new_name = str(new_name)

            with open(new_name, 'wb') as p:
                p.write(f.read())
                
        print("Success!")
