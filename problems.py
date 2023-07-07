import random
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
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
    choice for difficulty, ranging from 1 to 6. If the user enters a valid 
    integer, it is returned with this function."""
    with open("difficulty.txt", "r") as f:
        difficulty_settings = f.readlines()
    print("".join(difficulty_settings))
    user_setting = ""
    while (not isinstance(user_setting, int) or user_setting > 6 or 
           user_setting < 1):
        user_setting = int(input("Choose a difficulty setting: \n>: "))
        if not isinstance(user_setting, int):
            print("TypeError: difficulty argument should be an integer.")
        elif (user_setting > 6 or user_setting < 1):
            print("ValueError: difficulty should be between 1 and 6.")
    return user_setting

def get_problem(difficulty: int = 1) -> tuple:
    """Returns a tuple containing a random equation generated from a 
    difficulty setting and its solution."""
    if isinstance(difficulty, int):
        x = y = 0
        match difficulty:
            case 1:
                x, y = [random.randint(1, 9) for n in range(2)]
            case 2:
                x = random.randint(10, 99)
                y = random.randint(1, 9)
            case 3:
                x = random.randint(100, 999)
                y = random.randint(1, 9)
            case 4:
                x, y = [random.randint(10, 99) for n in range(2)]
            case 5:
                x = random.randint(10, 99)
                y = random.randint(100, 999)
            case 6:
                x, y = [random.randint(100, 999) 
                        for n in range(2)]
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
        print(f"The answer was {solution}.")
        return False
    
def set_leaderboard(username: str, score: int, difficulty: int, 
                    elapsed_time: float) -> None:
    """Writes the user's name, a timestamp in ISO format, their score, and the 
    elapsed time of the quiz to leaderboard.txt."""
    with open("leaderboard.csv", "a") as f:
        f.write(f"{username},{datetime.now().isoformat()}," +
                f"{score},{difficulty},{elapsed_time}\n")
    print("Score saved.")

def get_leaderboard() -> None:
    """Retrieves the first five rows of the leaderboard and prints it to the 
    console."""
    leaderboard = pd.read_csv("leaderboard.csv")
    top_ten = leaderboard.sort_values(["Difficulty", "Score", "Elapsed Time"], 
                                      ascending=[False, False, True])
    top_ten = top_ten.reset_index(drop=True)
    print("===Leaderboard===")
    print(top_ten.head(5))

def get_progress(username: str, difficulty: int) -> None:
    """Takes a username as an argument and displays a line graph showing the 
    change in the user's score and elapsed time per round over time."""
    leaderboard = pd.read_csv("leaderboard.csv")
    user_data = pd.DataFrame(leaderboard[
        (leaderboard["Username"] == username) & 
        (leaderboard["Difficulty"] == difficulty)])
    user_data["Timestamp"] = user_data["Timestamp"].apply(
        lambda x: pd.to_datetime(x))
    plt.style.use('dark_background')
    fig, axs = plt.subplots(2, 1)
    fig.suptitle(f"{username} - Scores")
    axs[0].plot(user_data["Timestamp"], user_data["Score"])
    axs[0].set_ylabel("Score")
    axs[0].tick_params(axis='x', rotation=45)
    axs[1].plot(user_data["Timestamp"], user_data["Elapsed Time"])
    axs[1].set_xlabel("Date & Time")
    axs[1].set_ylabel("Time Taken")
    axs[1].tick_params(axis='x', rotation=45)
    fig.tight_layout()
    plt.show()
