"""


WARNING !

THIS METHOD IS STILL UNSTABLE, PLEASE DO NOT USE IT BEFORE RELEASE ON PYPI!


"""



import whitehat

chrome = whitehat.Browser(browser_name="Chrome")
print(chrome.get_all_history())
