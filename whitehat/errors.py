class WhitehatErrors(Exception):
    def __init__(self, message:str=None):
        if message is None:
            message = 'An unknown error has occurred within Whitehat.'
        super().__init__(message)
        
class InvalidFormat(WhitehatErrors):
    def __init__(self):
        super().__init__("Invalid Format. Supported formats : 'list', 'json'.")

class DatabaseLocked(WhitehatErrors):
    def __init__(self, browser:str="your browser"):
        super().__init__(f"Database is locked. Make sure {browser} is closed!")

class InvalidIP(WhitehatErrors):
    def __init__(self):
        super().__init__("Invalid IP. Cannot include: http:// or https://")

class InvalidURL(WhitehatErrors):
    def __init__(self):
        super().__init__("Invalid URL. Cannot include: http:// or https://")

class UnsupportedOS(WhitehatErrors):
    def __init__(self, OS:str="Your OS", supported_os:str=None):
        super().__init__(f"{OS} is not supported on this function. Supported OS : {supported_os}.")

class CannotNone(WhitehatErrors):
    def __init__(self, parameter:str=None):
        super().__init__(f"'{parameter}' parameter cannot None.")

class UnsupportedBrowser(WhitehatErrors):
    def __init__(self, Browser:str="Your Browser"):
        super().__init__(f"{Browser} is not supported on this function.")

class ShiftExceededTheLimit(WhitehatErrors):
    def __init__(self, number:int=25):
        super().__init__(f"Shift cannot more than {number}.")

class InstallAdditionalPackages(WhitehatErrors):
    def __init__(self, packages:str="additional"):
        super().__init__(f"\n\nYou must install {packages} packages.\ntry 'whitehat.install_additional_packages()' or https://github.com/EterNomm/Whitehat/blob/main/additional_packages.txt")
