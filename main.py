import app
import soundtrack
import os

if os.getcwd()[-19:]:
    media = soundtrack.Soundtrack()
    game = app.App(media)
else:
    print("Error: Make sure that the current working directory is "
    "the '/arithmetic-speedrun' folder.")
