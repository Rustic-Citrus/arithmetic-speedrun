import classes
import setup
import time

if setup.check_cwd():
    print(setup.introduction())
    media = classes.MediaFiles()
    game = classes.App()
    username = input("Choose a username.\n>: ")
    play_again = "Y"
    while game:
        operation = setup.operation()
        difficulty = setup.difficulty()
        problem_count = setup.problem_count()
        new_round = classes.Game(problem_count, difficulty, username, 
                                 time.time(), operation)
        new_round.play_round(media)
        if input("Would you like to save your score? "
                 "(press Y).\n>: ").upper() == "Y":
            new_round.save_score()
        if (input("Would you like to see how your score has changed over "
                   "time? (press Y)\n>: ").upper() == "Y"):
            new_round.view_graph()
        play_again = input("Would you like to play again? (press Y)\n>: ")
    print("Thanks for playing!")
else:
    print("Error: Make sure that the current working directory is "
          "the '/arithmetic-speedrun' folder.")
