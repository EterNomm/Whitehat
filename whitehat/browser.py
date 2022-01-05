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

    Supported Browser :
    - Chrome
    """

    def __init__(self, browser_name:str):
        self.browser_name = browser_name
        self.os = platform.uname()[0]

    def get_history(self, show:int="all"):
        r"""
        Get history of your browser
        ---
        Parameter :
        - show: `int` | How much history should be displayed (Default : all)
        ---
        Supported OS :
        - Windows
        - Linux (Unstable)
        """
        browser_name = self.browser_name
        self_os = self.os

        chrome = ["chrome", "Chrome"]

        if any(v in browser_name for v in chrome):
            if self_os == "Windows":
                data_path = os.path.expanduser('~')+"\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
                
                temp_path = os.path.expanduser('~')+"\\AppData\\Local\\Temp"
                
                shutil.copyfile(os.path.join(data_path, 'History'),os.path.join(temp_path,'History.db'))
                
                db_path = os.path.join(temp_path,'History.db')
                connect = sqlite3.connect(db_path)
                c = connect.cursor()

                sql_sort = """
                SELECT url,
                datetime(last_visit_time/1000000-11644473600,'unixepoch','localtime'),
                visit_count FROM urls
                """

                try:
                    c.execute(sql_sort)
                except sqlite3.OperationalError:
                    raise DatabaseLocked

                if show == "all":
                    results = c.fetchall()
                else:
                    results = c.fetchmany(show)

                list_num = 0

                for r in results:
                    list_num = list_num+1
                    r = str(r)
                    r = r.replace("(", "")
                    r = r.replace(")", "")
                    r = r.replace("'", "")

                    print(f"{list_num} | {r}")
                    
                c.close()

            elif self_os == "Linux":

                db_path = os.path.expanduser('~')+"/.config/google-chrome/Default/History"

                connect = sqlite3.connect(db_path)
                c = connect.cursor()
                 
                sql_sort = """
                SELECT url,
                datetime(last_visit_time/1000000-11644473600,'unixepoch','localtime'),
                visit_count FROM urls
                """

                try:
                    c.execute(sql_sort)
                except sqlite3.OperationalError:
                    raise DatabaseLocked

                if show == "all":
                    results = c.fetchall()
                else:
                    results = c.fetchmany(show)

                list_num = 0

                for r in results:
                    list_num = list_num+1
                    r = str(r)
                    r = r.replace("(", "")
                    r = r.replace(")", "")
                    r = r.replace("'", "")

                    print(f"{list_num} | {r}")
                    
                c.close()
            
            else:
                raise UnsupportedOS(supported_os="Windows, Linux")
            
        else:
            raise UnsupportedBrowser
