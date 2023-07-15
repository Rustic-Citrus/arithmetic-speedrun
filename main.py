import app
import soundtrack
import os

if os.getcwd()[-19:]:
    print("Starting game...")
    media = soundtrack.Soundtrack()
    game = app.App(media)
    print("Thanks for playing!")
else:
    print("Error: Make sure that the current working directory is "
          "the '/arithmetic-speedrun' folder.")
