"""


WARNING !

THIS METHOD IS STILL UNSTABLE, PLEASE DO NOT USE IT BEFORE RELEASE ON PYPI!


"""



import whitehat

chrome = whitehat.Browser("Chrome")
chrome.get_history(show=100) # Default : all
