
# PLEASE READ https://github.com/EterNomm/Whitehat/blob/main/examples/png_and_jpg.md !!!

import whitehat

# Hide message
jpg = whitehat.JPG("file.jpg")
jpg.hide_message("Super Secret Message")

# Reveal secret messages
reveal_jpg = whitehat.JPG("file.jpg")
print(reveal_jpg.reveal_message())

# Hide program
program = whitehat.JPG("file.jpg")
program.hide_program("App.exe")

# Reveal Program
reveal_program = whitehat.JPG("file.jpg")
reveal_program.reveal_program("NewApp.exe")
