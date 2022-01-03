import os
import sqlite3
import platform
import shutil

from .errors import *

class Browser:
    r"""A class that implements Browser function
    -----------
    Parameters :
    - browser_name: :class:`str` | Set browser name

    Browser support :
    - Chrome
    """

    def __init__(self, browser_name:str):
        self.browser_name = browser_name
        self.os = platform.uname()[0]

    def get_all_history(self):
        r"""
        Get all history of your browser
        """
        browser_name = self.browser_name
        self_os = self.os

        chrome = ["chrome", "Chrome"]

        if any(v in browser_name for v in chrome):
            if self_os == "Windows":
                data_path = os.path.expanduser('~')+"\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
                files = os.listdir(data_path)
                
                temp_path = os.path.expanduser('~')+"\\AppData\\Local\\Temp"
                
                shutil.copyfile(os.path.join(data_path, 'History'),os.path.join(temp_path,'History.db'))
                
                history_db = os.path.join(temp_path,'History.db')
                con = sqlite3.connect(history_db)
                c = con.cursor()
                
                c.execute("select url, visit_count, last_visit_time from urls")
                results = c.fetchall()
                
                for r in results:
                    r = str(r)
                    r = r.replace("(", "")
                    r = r.replace(")", "")
                    r = r.replace("'", "")
                    r = r.replace(",", " -")
                    print(r)
                    
                c.close()
            
            else:
                raise UnsupportedOS(supported_os="Windows")
            
        else:
            raise UnsupportedBrowser
