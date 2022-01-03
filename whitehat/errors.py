class WhitehatErrors(Exception):
    def __init__(self, message:str=None):
        if message is None:
            message = 'An error has occurred within Whitehat'
        super().__init__(message)
        
class InvalidFormat(WhitehatErrors):
    def __init__(self):
        super().__init__("Invalid Format. Supported formats : 'list', 'json'")

class DatabaseLocked(WhitehatErrors):
    def __init__(self, browser:str="Chrome"):
        super().__init__(f"Error : Database is locked. Make sure {browser} is closed!")

class InvalidIP(WhitehatErrors):
    def __init__(self):
        super().__init__("Invalid IP. Cannot include: http:// or https://")

class InvalidURL(WhitehatErrors):
    def __init__(self):
        super().__init__("Invalid URL. Cannot include: http:// or https://")

class UnsupportedOS(WhitehatErrors):
    def __init__(self, OS:str="Your OS", supported_os:str=None):
        super().__init__(f"Error : {OS} is not supported on this function. Supported OS : {supported_os}")

class CannotNone(WhitehatErrors):
    def __init__(self, parameter: str = None):
        super().__init__(f"Error : '{parameter}' cannot None")

class UnsupportedBrowser(WhitehatErrors):
    def __init__(self, Browser:str="Your Browser", supported_os:str=None):
        super().__init__(f"Error : {Browser} is not supported on this function.")
