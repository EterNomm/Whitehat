from .ddos import *
from .phonenumber import *
from .wifi import *
from .ip import *
from .keylogger import *
from .port import *
from .reverse_shell import *
from .browser import *
from .bruteforce import *
from .cryptography import *

__title__ = "Whitehat"
__version__ = "1.2.1"
__authors__ = "LyQuid and EterNomm"
__license__ = "Apache License 2.0"
__copyright__ = "Copyright 2021-present EterNomm"


import subprocess
import os

def install_additional_packages():
    os.system("pip install pynput==1.7.4")
    install = subprocess.check_output("pip install pynput==1.7.4", shell=True)
    print(install.decode())
