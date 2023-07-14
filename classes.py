import random
from datetime import datetime
import time
import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
import pyglet

HEADING = ("MS Gothic", 18)
BODY = ("MS Gothic", 14)

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
        self.problem_total = problem_count
        self.problem_counter = 0
        self.correct_answers = 0
        self.score = 0
        self.username = username
        self.elapsed_time = .0
        self.operation = operation[0]
        self.operator = operation[1]
        self.operation_name = None
        self.equations_seen = list()
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
        while self.problem_counter < self.problem_total:
            for n in range(self.problem_total):
                response = self.ask_question()
                if response[0] == response[1]:
                    self.correct_answers += 1
                    media.play_sound("correct_answer")
                else:
                    media.play_sound("incorrect_answer")
                self.problem_counter += 1
        correct_ratio = self.correct_answers / self.problem_counter
        self.elapsed_time = round(time.time() - self.start_time, 3)
        self.score = int(((self.difficulty * correct_ratio * self.problem_total
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
        equation = reverse_equation = solution = None
        equation_is_new = False
        while not equation_is_new:
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
            reverse_equation = f"{y} {self.operator} {x} = x"
            if ((equation not in self.equations_seen) and 
                (reverse_equation not in self.equations_seen)):
                equation_is_new = True
                self.equations_seen.append(equation)
                self.equations_seen.append(reverse_equation)
            else:
                continue
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


class App(Game):
    def __init__(self, root=tk.Tk()):
        self.root = root
        self.root.title("ArithmeticSpeedrun")
        self.root.geometry("400x600")
        self.root.resizable(0, 0)

    def get_start_menu(self):
        self.start_menu = tk.Frame(self.root)
        greeting = tk.Label(self.start_menu, 
                            text="Welcome\nto\nArithmetic Speedrun!", 
                            font=HEADING)
        greeting.grid(row=0, pady=(0, 20))
        start = tk.Button(self.start_menu, text="Start", 
                          font=BODY, 
                          command=self.get_choose_username)
        start.grid(row=1, pady=(0, 20))
        instructions = tk.Button(self.start_menu, text="Instructions", 
                                 font=BODY)
        instructions.grid(row=2, pady=(0, 20))
        leaderboard = tk.Button(self.start_menu, text="Leaderboard", 
                                font=BODY)
        leaderboard.grid(row=3, pady=(0, 100))
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.start_menu.grid()
        self.root.mainloop()

    def get_choose_username(self):
        self.start_menu.grid_remove()
        self.choose_username = tk.Frame(self.root)
        prompt = tk.Label(self.choose_username, text="Choose your username:", 
                          font=HEADING)
        prompt.grid(row=0, pady=(0, 20))
        global username_entry
        username_entry = tk.Entry(self.choose_username, font=BODY)
        username_entry.grid(row=1, pady=(0, 0))
        next = tk.Button(self.choose_username, text="Next", 
                           font=BODY, command=self.get_choose_operation)
        next.grid(row=3, pady=(100, 40))
        self.choose_username.grid()
        
    def get_choose_operation(self):
        self.username = username_entry.get()
        self.choose_username.grid_remove()
        self.choose_operation = tk.Frame(self.root)
        prompt = tk.Label(self.choose_operation, text="Choose an operation:", 
                          font=HEADING)
        prompt.grid(row=0, pady=(0, 20))
        addition = tk.Button(self.choose_operation, text="Addition", font=BODY)
        addition.grid(row=1, pady=(0, 20))
        subtraction = tk.Button(self.choose_operation, text="Subtraction", 
                                font=BODY)
        subtraction.grid(row=2, pady=(0, 20))
        multiplication = tk.Button(self.choose_operation, 
                                   text="Multiplication", font=BODY)
        multiplication.grid(row=3, pady=(0, 20))
        division = tk.Button(self.choose_operation, text="Division", font=BODY)
        division.grid(row=4, pady=(0, 20))
        self.choose_operation.grid()

    def end_round(self, game):
        self.save_button = tk.Button(self.root, text="Save Score",
                                     command=game.save_score)

my_app = App()
my_app.get_start_menu()
