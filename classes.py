import random
from datetime import datetime
import time
import pandas as pd
import matplotlib.pyplot as plt
import pyglet

class MediaFiles:
    def __init__(self) -> None:
        self.correct_answer_sound = pyglet.media.load(
            ("media/correct_answer.wav"), streaming=False)
        self.incorrect_answer_sound = pyglet.media.load(
            ("media/incorrect_answer.wav"), streaming=False)
        self.high_score_sound = pyglet.media.load(
            ("media/high_score_sound.wav"), streaming=False)
        self.low_score_sound = pyglet.media.load(("media/low_score_sound.wav"),
                                            streaming=False)
        
    def play_sound(self, sound: str) -> None:
        """Takes a string as an argument and plays the corresponding sound."""
        match sound:
            case "correct_answer":
                self.correct_answer_sound.play()
            case "incorrect_answer":
                self.incorrect_answer_sound.play()
            case "high_score":
                self.high_score_sound.play()
            case "low_score":
                self.low_score_sound.play()

class Game:
    def __init__(self, problem_count: int, 
                 difficulty: int, start_time) -> None:
        self.start_time = start_time
        self.difficulty = difficulty
        self.problem_count = problem_count
        self.counter = 0
        self.correct = 0
        self.score = 0
        self.username = ""
        self.elapsed_time = .0

    def play_round(self, media) -> None:
        while self.counter < self.problem_count:
            for n in range(self.problem_count):
                response = self.ask_question()
                if response[0] == response[1]:
                    self.correct += 1
                    media.play_sound("correct_answer")
                else:
                    media.play_sound("incorrect_answer")
                self.counter += 1
        self.score = (self.correct / self.counter) * 100
        self.elapsed_time = round(time.time() - self.start_time, 3)
        if self.score >= 80:
            media.play_sound("high_score")
        else:
            media.play_sound("low_score")
        print(f"\rElapsed time: {self.elapsed_time} seconds")
        print(f"You scored {self.score}%.")
        self.get_leaderboard()

    def ask_question(self) -> tuple:
        """Takes a get_question() tuple, requests the solution from the user, 
        compares the actual input with the expected input, then returns either 
        True or False depending on whether the user gets the question right."""
        x = y = 0
        match self.difficulty:
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
        print(equation)
        response = int(input("x = "))
        if response == solution:
            print("Correct!")
        else:
            print("Incorrect.")
            print(f"The answer was {solution}.")
        return (response, solution)
        
    def save_score(self) -> None:
        """Writes the user's name, a timestamp in ISO format, their score, and 
        the elapsed time of the quiz to leaderboard.txt."""
        with open("leaderboard.csv", "a") as f:
            f.write(f"{self.username},{datetime.now().isoformat()}," +
                    f"{self.score},{self.difficulty},{self.elapsed_time}\n")
        print("Score saved.")

    def get_leaderboard(self) -> None:
        """Retrieves the first five rows of the leaderboard and prints it to 
        the console."""
        leaderboard = pd.read_csv("leaderboard.csv")
        top_ten = leaderboard.sort_values(
            ["Difficulty", "Score", "Elapsed Time"], 
            ascending=[False, False, True])
        top_ten = top_ten.reset_index(drop=True)
        print("===Leaderboard===")
        print(top_ten.head(5))

    def view_graph(self) -> None:
        """Takes a username as an argument and displays a line graph showing 
        the change in the user's score and elapsed time per round over time."""
        leaderboard = pd.read_csv("leaderboard.csv")
        user_data = pd.DataFrame(leaderboard[
            (leaderboard["Username"] == self.username) & 
            (leaderboard["Difficulty"] == self.difficulty)])
        user_data["Timestamp"] = user_data["Timestamp"].apply(
            lambda x: pd.to_datetime(x))
        plt.style.use('dark_background')
        fig, axs = plt.subplots(2, 1)
        fig.suptitle(f"{self.username} - Scores")
        axs[0].plot(user_data["Timestamp"], user_data["Score"])
        axs[0].set_ylabel("Score")
        axs[0].tick_params(axis='x', rotation=45)
        axs[1].plot(user_data["Timestamp"], user_data["Elapsed Time"])
        axs[1].set_xlabel("Date & Time")
        axs[1].set_ylabel("Time Taken")
        axs[1].tick_params(axis='x', rotation=45)
        fig.tight_layout()
        plt.show()
