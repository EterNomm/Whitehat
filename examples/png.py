
# PLEASE READ https://github.com/EterNomm/Whitehat/blob/main/examples/png_and_jpg.md !!!

import whitehat

# Hide message
png = whitehat.PNG("file.png")
png.hide_message("Super Secret Message")

# Reveal secret messages
reveal_png = whitehat.PNG("file.png")
print(reveal_png.reveal_message())

# Hide program
program = whitehat.PNG("file.png")
program.hide_program("App.exe")

# Reveal Program
reveal_program = whitehat.PNG("file.png")
reveal_program.reveal_program("NewApp.exe")
