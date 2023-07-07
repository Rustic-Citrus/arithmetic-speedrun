import classes
import setup
import time

print(setup.introduction())
media = classes.MediaFiles()
username = input("Choose a username.\n>: ")
play_again = "Y"
while play_again.upper() == "Y":
    difficulty = setup.difficulty()
    problem_count = setup.problem_count()
    new_round = classes.Game(problem_count, difficulty, username, time.time())
    new_round.play_round(media)
    new_round.save_score() if (input("Would you like to save your score? (press Y).\n>: ").upper() == "Y") else None
    new_round.view_graph() if (input("Would you like to see how your score has changed over time? (press Y)\n>: ").upper() == "Y") else None
    play_again = input("Would you like to play again? (press Y)\n>: ")
print("Thanks for playing!")
