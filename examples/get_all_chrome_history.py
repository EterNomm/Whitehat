"""


WARNING !

THIS METHOD IS STILL UNSTABLE, PLEASE DO NOT USE IT BEFORE RELEASE ON PYPI!


"""



import whitehat

history = whitehat.Browser(browser_name="Chrome")
print(history.get_all_history())