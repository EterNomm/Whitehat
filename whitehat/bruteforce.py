import zipfile
from tqdm import tqdm

from .errors import *

class BruteForce:
    r"""A class that implements Brute Force function
    -----------
    Parameters :
    - wordlist: :class:`str` | Set wordlist to run Brute Force
    """

    def __init__(self, wordlist:str=None):
        if wordlist == None:
            raise CannotNone("wordlist")
        else:
            self.wodlist = wordlist

    def zip(self, zip_path:str=None):
        r"""A method that implements the Brute Force function on Zip
        -----------
        Parameters :
        - zip_path: :class:`str` | Set Zip file path
        """
        if zip_path == None:
            raise CannotNone("zip_path")

        wordlist = self.wodlist

        zip_file = zipfile.ZipFile(zip_path)
        
        n_words = len(list(open(wordlist, "rb")))
        print("Total passwords to test:", n_words)

        with open(wordlist, "rb") as wordlist:
            for word in tqdm(wordlist, total=n_words, unit="word"):
                try:
                    zip_file.extractall(pwd=word.strip())
                except:
                    continue
                else:
                    return "Password found:", word.decode().strip()
                    
        return "Password not found, try other wordlist."
