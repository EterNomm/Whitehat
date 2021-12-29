class WhitehatErrors(Exception):
    def __init__(self, message:str=None):
        if message is None:
            message = 'An error has occurred within Whitehat'
        super().__init__(message)
