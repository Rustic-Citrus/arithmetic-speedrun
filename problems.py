import random
from datetime import datetime
import pandas as pd
import pyglet

correct_answer_sound = pyglet.media.load("media/correct_answer.wav",
                                            streaming=False)
incorrect_answer_sound = pyglet.media.load("media/incorrect_answer.wav",
                                            streaming=False)
high_score_sound = pyglet.media.load("media/high_score_sound.wav",
                                     streaming=False)
low_score_sound = pyglet.media.load("media/low_score_sound.wav",
                                    streaming=False)

def get_difficulty() -> int:
    """Reads the difficulty settings to the user and requests an integer 
    choice for difficulty, ranging from 1 to 4. If the user enters a valid 
    integer, it is returned with this function."""
    with open("difficulty.txt", "r") as f:
        difficulty_settings = f.readlines()
    print("".join(difficulty_settings))
    user_setting = ""
    while (not isinstance(user_setting, int) or user_setting > 4 or 
           user_setting < 1):
        user_setting = int(input("Choose a difficulty setting: \n>: "))
        if not isinstance(user_setting, int):
            print("TypeError: difficulty argument should be an integer.")
        elif (user_setting > 4 or user_setting < 1):
            print("ValueError: difficulty should be between 1 and 4.")
    return user_setting

def get_problem(difficulty: int = 1) -> tuple:
    """Returns a tuple containing a random equation generated from a 
    difficulty setting and its solution."""
    if isinstance(difficulty, int):
        x = y = 0
        match difficulty:
            case 1:
                x, y = [random.randint(1, 10) for n in range(2)]
            case 2:
                x, y = [random.randint(10, 100) for n in range(2)]
            case 3:
                x, y = [random.randint(100, 1000) for n in range(2)]
            case 4:
                x, y = [random.randint(1000, 10000) for n in range(2)]
        solution = x * y
        equation = f"{x} * {y} = x"
        return (equation, solution)
    else:
        raise TypeError("The difficulty argument should be an integer.")

def get_input(problem: tuple) -> bool:
    """Takes a get_question() tuple, requests the solution from the user, 
    compares the actual input with the expected input, then returns either 
    True or False depending on whether the user gets the question right."""
    equation, solution = problem
    print(equation)
    response = int(input("x = "))
    if response == solution:
        print("Correct!")
        return True
    else:
        print("Incorrect.")
        return False
    
def set_leaderboard(username: str, score: int, difficulty: int, 
                    elapsed_time: float) -> None:
    """Writes the user's name, a timestamp in ISO format, their score, and the 
    elapsed time of the quiz to leaderboard.txt."""
    with open("leaderboard.csv", "a") as f:
        f.write(f"{username},{datetime.now().isoformat()}," +
                f"{score},{difficulty},{elapsed_time}\n")
    print("Score saved.")

def get_leaderboard():
    """Retrieves the first five rows of the leaderboard and prints it to the 
    console."""
    leaderboard = pd.read_csv("leaderboard.csv")
    top_ten = leaderboard.sort_values(["difficulty", "score", "elapsed time"], 
                                      ascending=[False, False, True])
    print("===Leaderboard===")
    print(top_ten.head(5))
