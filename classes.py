import random
from datetime import datetime
import time
import pandas as pd
import matplotlib.pyplot as plt
import pyglet

class MediaFiles:
    def __init__(self) -> None:
        """Initializes a MediaFiles instance with loaded sound files for game 
        feedback."""
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
    def __init__(self, problem_count: int, difficulty: int, username: str, 
                 start_time, operation) -> None:
        """Initializes a new Game instance with specific problem count, 
        difficulty, and user data."""
        self.start_time = start_time
        self.difficulty = difficulty
        self.problem_count = problem_count
        self.problems_seen = 0
        self.correct_answers = 0
        self.score = 0
        self.username = username
        self.elapsed_time = .0
        self.operation = operation[0]
        self.operator = operation[1]
        self.operation_name = None
        match self.operator:
            case "+":
                self.operation_name = "Addition"
            case "-":
                self.operation_name = "Subtraction"
            case "*":
                self.operation_name = "Multiplication"
            case "/":
                self.operation_name = "Division"

    def play_round(self, media) -> None:
        """Plays a round of the game, calculates the score, and updates the 
        leaderboard."""
        while self.problems_seen < self.problem_count:
            for n in range(self.problem_count):
                response = self.ask_question()
                if response[0] == response[1]:
                    self.correct_answers += 1
                    media.play_sound("correct_answer")
                else:
                    media.play_sound("incorrect_answer")
                self.problems_seen += 1
        correct_ratio = self.correct_answers / self.problems_seen
        self.elapsed_time = round(time.time() - self.start_time, 3)
        self.score = int(((self.difficulty * correct_ratio * self.problem_count
                          * 10) / self.elapsed_time) * 100)
        if correct_ratio >= 0.8:
            media.play_sound("high_score")
        else:
            media.play_sound("low_score")
        print(f"\rElapsed time: {self.elapsed_time} seconds")
        print(f"Your score was {self.score}!")
        self.get_leaderboard()

    def ask_question(self) -> tuple:
        """Generates a arithmetic problem, assesses user's answer, and 
        returns a tuple of user's and correct answers."""
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
        solution = self.operation(x, y)
        equation = f"{x} {self.operator} {y} = x"
        print(equation)
        response = None
        while response is None:
            try:
                response = float(input("x = "))
                if response == solution:
                    print("Correct!")
                else:
                    print("Incorrect.")
                    print(f"The answer was {solution}.")
            except ValueError:
                print("ValueError: Type the solution as a number.")
        return (response, solution)
        
    def save_score(self) -> None:
        """Saves the user's score, difficulty, and time to the leaderboard 
        CSV."""
        with open("leaderboard.csv", "a") as f:
            f.write(
                f"{self.username},{datetime.now().isoformat()},{self.score},"
                f"{self.difficulty},{self.operation_name},"
                f"{self.elapsed_time}\n")
        print("Score saved.")

    def get_leaderboard(self) -> None:
        """Retrieves the first five rows of the leaderboard and prints it to 
        the console."""
        leaderboard = pd.read_csv("leaderboard.csv")
        top_ten = leaderboard.sort_values(
            ["Score", "Difficulty", "Elapsed Time"], 
            ascending=[False, False, True])
        top_ten = top_ten.reset_index(drop=True)
        print("===Leaderboard===")
        print(top_ten.head(5))

    def view_graph(self) -> None:
        """Generates and displays a graph of the user's scores."""
        leaderboard = pd.read_csv("leaderboard.csv")
        user_data = pd.DataFrame(leaderboard[
            (leaderboard["Username"] == self.username) &
            (leaderboard["Difficulty"] == self.difficulty) &
            (leaderboard["Operation"] == self.operation_name)])
        user_data["Timestamp"] = user_data["Timestamp"].apply(
            lambda x: pd.to_datetime(x))
        plt.style.use('dark_background')
        fig, ax = plt.subplots(1, 1)
        fig.suptitle(f"{self.username} - Scores for {self.operation_name}")
        ax.plot(user_data["Timestamp"], user_data["Score"], 
                    color="#FFFF00")
        ax.scatter(user_data["Timestamp"], user_data["Score"], 
                    color="#FFFFFF")
        ax.set_ylabel("Score")
        ax.tick_params(axis='x', rotation=45)
        ax.set_xlabel("Date & Time")
        ax.tick_params(axis='x', rotation=45)
        fig.tight_layout()
        plt.show()
