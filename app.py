import random
from datetime import datetime
import time
import operator
import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt

HEADING = ("MS Gothic", 18)
BODY = ("MS Gothic", 14)

difficulty_dict = {1: "Easy", 2: "Basic", 3: "Medium", 4: "Moderate",
                   5: "Challenging", 6: "Hard"}
operation_dict = {"Addition": operator.add, "Subtraction": operator.sub, 
                  "Multiplication": operator.mul, "Division": operator.truediv}
operator_dict = {"Addition": "+", "Subtraction": "-", 
                  "Multiplication": "×", "Division": "÷"}


class Game:
    def __init__(self, media) -> None:
        """Initializes a new Game instance with specific problem count, 
        difficulty, and user data."""
        self.media = media
        self.start_time = .0
        self.difficulty = 0
        self.problem_total = 5
        self.problem_counter = 0
        self.correct_answers = 0
        self.correct_ratio = .0
        self.score = 0
        self.equation = None
        self.solution = None
        self.username = None
        self.operation_name = "Addition"
        self.elapsed_time = .0
        self.operation = operation_dict[self.operation_name]
        self.operator = operator_dict[self.operation_name]
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

    def set_operation(self, operation_name):
        self.operation_name = operation_name
        self.operation = operation_dict[self.operation_name]
        self.operator = operator_dict[self.operation_name]
    
    def get_elapsed_time(self):
        self.elapsed_time = round(time.time() - self.start_time, 3)
        return self.elapsed_time

    def get_results(self):
        if self.correct_ratio >= 0.8:
            self.media.play_sound("high_score")
            return "Congratulations"
        else:
            self.media.play_sound("low_score")
            return "Try again"
        
    def get_instructions(self) -> str:
        """Read README.md and output the contents as a string."""
        with open("README.md", "r") as f:
            readme = f.readlines()
        intro = "".join(readme)
        return intro

    def generate_question(self) -> tuple:
        """Generates a arithmetic problem, assesses user's answer, and 
        returns a tuple of user's and correct answers."""
        x = y = 0
        equation = reverse_equation = solution = None
        equation_tuple = tuple()
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
                equation_tuple = (equation, solution)
            else:
                continue
        return equation_tuple

    def check_answer(self, response, solution):
        try:
            if response == solution:
                return True
            else:
                return False
        except ValueError:
            print("ValueError: Type the solution as a number.")
        
    def save_score(self) -> None:
        """Saves the user's score, difficulty, and time to the leaderboard 
        CSV."""
        with open("leaderboard.csv", "a") as f:
            f.write(
                f"{self.username},{datetime.now().isoformat()},{self.score},"
                f"{self.difficulty},{self.operation_name},"
                f"{self.elapsed_time}\n")
        print("Score saved.")

    def get_leaderboard(self):
        """Reads, sorts and returns the leaderboard."""
        leaderboard = pd.read_csv("leaderboard.csv")
        top_ten = leaderboard.sort_values(
            ["Score", "Difficulty", "Elapsed Time"], 
            ascending=[False, False, True])
        top_ten = top_ten.reset_index(drop=True)
        return top_ten

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
    def __init__(self, media, root=tk.Tk()):
        """Creates an instance of an App class."""
        super().__init__(media)
        self.root = root
        self.root.title("ArithmeticSpeedrun")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        self.get_main_menu_frame()
        self.media.play_sound("startup")
        self.root.mainloop()

    def get_main_menu_frame(self):
        """Displays the main_menu_frame."""
        def start_function():
            """Removes the main_menu_frame and displays the 
            username_frame_frame."""
            main_menu_frame.grid_remove()
            self.get_username_frame()
            self.media.play_sound("click_button")

        def instructions_function():
            """Removes the main_menu_frame and displays the 
            instructions_frame."""
            main_menu_frame.grid_remove()
            self.get_instructions_frame()
            self.media.play_sound("click_button")

        def leaderboard_function():
            """Removes the main_menu_frame and displays the 
            leaderboard_frame."""
            main_menu_frame.grid_remove()
            self.get_leaderboard_frame()
            self.media.play_sound("click_button")

        main_menu_frame = tk.Frame(self.root)
        greeting_label = tk.Label(main_menu_frame,
                                  text="Welcome\nto\nArithmetic Speedrun!",
                                  font=HEADING)
        greeting_label.grid(row=0, pady=(0, 20))
        start_button = tk.Button(main_menu_frame, text="Start",
                                 font=BODY, command=start_function)
        start_button.grid(row=1, pady=(0, 20))
        instructions_button = tk.Button(main_menu_frame, text="Instructions",
                                        font=BODY, 
                                        command=instructions_function)
        instructions_button.grid(row=2, pady=(0, 20))
        leaderboard_button = tk.Button(main_menu_frame, text="Leaderboard",
                                       font=BODY, command=leaderboard_function)
        leaderboard_button.grid(row=3, pady=(0, 40))
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        main_menu_frame.grid()
    
    def get_instructions_frame(self):
        def main_menu_function():
            instructions_frame.grid_remove()
            self.get_main_menu_frame()
            self.media.play_sound("click_button")

        instructions = self.get_instructions()
        instructions_frame = tk.Frame(self.root)
        title_label = tk.Label(instructions_frame, text="Instructions", 
                               font=HEADING)
        title_label.grid(row=0, pady=(0, 20))
        instructions_text = tk.Text(instructions_frame,
                                    font=("Arial", 12), width=40, 
                                    wrap="word")
        instructions_text.insert(tk.END, instructions)
        instructions_text.config(state="disabled")
        instructions_text.grid(row=1, column=0, pady=(0, 20))
        scrollbar = tk.Scrollbar(instructions_frame, 
                                 command=instructions_text.yview)
        scrollbar.grid(row=1, column=1, sticky="nsew")
        main_menu_button = tk.Button(instructions_frame, text="Main Menu", 
                                     font=BODY, command=main_menu_function)
        main_menu_button.grid(row=2, pady=(0, 20))
        instructions_frame.grid()

    def get_leaderboard_frame(self):
        def main_menu_function():
            leaderboard_frame.grid_remove()
            self.get_main_menu_frame()
            self.media.play_sound("click_button")

        leaderboard = self.get_leaderboard()
        leaderboard_frame = tk.Frame(self.root)
        title_label = tk.Label(leaderboard_frame, text="Leaderboard", 
                               font=HEADING)
        title_label.grid(row=0, pady=(20, 20))
        leaderboard_cols = leaderboard.columns.tolist()
        leaderboard_treeview = ttk.Treeview(leaderboard_frame, 
                                            columns=leaderboard_cols,
                                            show="headings")
        for column in leaderboard.columns:
            leaderboard_treeview.column(column, width=60)
            leaderboard_treeview.heading(column, text=column)
        for index, row in leaderboard[:10].iterrows():
            leaderboard_treeview.insert("", "end", values=list(row))
        leaderboard_treeview.grid(row=1, pady=(0, 20))
        main_menu_button = tk.Button(leaderboard_frame, text="Main Menu", 
                                     font=BODY, command=main_menu_function)
        main_menu_button.grid(row=2, column=0, padx=(0, 20))
        leaderboard_frame.grid()

    def get_username_frame(self):
        def next_function():
            self.username = username_entry.get()
            username_frame.grid_remove()
            self.get_operation_frame()
            self.root.bind("<Return>", lambda event: None)
            self.media.play_sound("click_button")

        def back_function():
            username_frame.grid_remove()
            self.get_main_menu_frame()
            self.root.bind("<Return>", lambda event: None)
            self.media.play_sound("click_button")
        
        self.root.bind("<Return>", lambda event: next_function())
        username_frame = tk.Frame(self.root)
        prompt_label = tk.Label(username_frame, text="Choose your username:", 
                                font=HEADING)
        prompt_label.grid(row=0, pady=(0, 20))
        username_entry = tk.Entry(username_frame, font=BODY)
        username_entry.grid(row=1, pady=(0, 20))
        buttons_frame = tk.Frame(username_frame)
        back_button = tk.Button(buttons_frame, text="Back",
                                font=BODY, command=back_function)
        back_button.grid(row=0, column=0, padx=(0, 20))
        next_button = tk.Button(buttons_frame, text="Next",
                                font=BODY, command=next_function)
        next_button.grid(row=0, column=1, padx=(20, 0))
        buttons_frame.grid(row=2, pady=(40, 20))
        username_frame.grid()
        username_entry.focus_set()
        
    def get_operation_frame(self):
        def next_function(operation):
            self.set_operation(operation)
            operation_frame.grid_remove()
            self.get_difficulty_frame()
            self.media.play_sound("click_button")

        def back_function():
            operation_frame.grid_remove()
            self.get_username_frame()
            self.media.play_sound("click_button")

        operation_frame = tk.Frame(self.root)
        prompt_label = tk.Label(operation_frame, text="Choose an operation:",
                                font=HEADING)
        prompt_label.grid(row=0, pady=(0, 20))
        addition_button = tk.Button(operation_frame, text="Addition", 
                                    font=BODY, 
                                    command=lambda: next_function("Addition"))
        addition_button.grid(row=1, pady=(0, 20))
        subtraction_button = tk.Button(operation_frame, 
                                       text="Subtraction", font=BODY,
                                       command=lambda: 
                                       next_function("Subtraction"))
        subtraction_button.grid(row=2, pady=(0, 20))
        multiplication_button = tk.Button(operation_frame,
                                          text="Multiplication", font=BODY,
                                          command=lambda:
                                          next_function("Multiplication"))
        multiplication_button.grid(row=3, pady=(0, 20))
        division_button = tk.Button(operation_frame, text="Division", 
                                    font=BODY, 
                                    command=lambda: next_function("Division"))
        division_button.grid(row=4, pady=(0, 20))
        back_button = tk.Button(operation_frame, text="Back", font=BODY, 
                                command=back_function)
        back_button.grid(row=5, pady=(40, 20))
        operation_frame.grid()

    def get_difficulty_frame(self):
        def update_difficulty_label(value):
            difficulty_label.config(
                text=difficulty_dict[int(value)])

        def next_function():
            self.difficulty = difficulty_slider.get()
            difficulty_frame.grid_remove()
            self.get_problems_frame()
            self.media.play_sound("click_button")

        def back_function():
            difficulty_frame.grid_remove()
            self.get_operation_frame()
            self.media.play_sound("click_button")

        difficulty_frame = tk.Frame(self.root)
        prompt_label = tk.Label(difficulty_frame, text="Choose a difficulty:",
                                font=HEADING)
        prompt_label.grid(row=0, pady=(0, 20))
        difficulty_label = tk.Label(difficulty_frame, text="", 
                                    font=HEADING)
        difficulty_label.grid(row=1, pady=(0, 20))
        difficulty_slider = tk.Scale(difficulty_frame, from_=1, to=6, 
                                     orient="horizontal", length=200, 
                                     command=update_difficulty_label, 
                                     width=20, relief=tk.FLAT)
        difficulty_slider.grid(row=2, pady=(0, 20))
        buttons_frame = tk.Frame(difficulty_frame)
        back_button = tk.Button(buttons_frame, text="Back",
                                font=BODY, command=back_function)
        back_button.grid(row=0, column=0, padx=(0, 20))
        next_button = tk.Button(buttons_frame, text="Next",
                                font=BODY, command=next_function)
        next_button.grid(row=0, column=1, padx=(20, 0))
        buttons_frame.grid(row=3, pady=(40, 20))
        difficulty_frame.grid()
        update_difficulty_label(difficulty_slider.get())

    def get_problems_frame(self):
        def next_function():
            self.problem_total = int(problems_slider.get())
            problems_frame.grid_remove()
            self.get_start_frame()
            self.media.play_sound("click_button")

        def back_function():
            problems_frame.grid_remove()
            self.get_difficulty_frame()
            self.media.play_sound("click_button")

        problems_frame = tk.Frame(self.root)
        self.root.bind("<Return>", lambda event: next_function())
        prompt_label = tk.Label(problems_frame, 
                          text="Choose the number of problems:",
                          font=HEADING)
        prompt_label.grid(row=0, pady=(0, 20))
        problems_slider = tk.Scale(problems_frame, from_=5, to=50,
                                   orient="horizontal", length=200)
        problems_slider.grid(row=1, pady=(0, 20))
        buttons_frame = tk.Frame(problems_frame)
        back_button = tk.Button(buttons_frame, text="Back", 
                                font=BODY, command=back_function)
        back_button.grid(row=0, column=0, padx=(0, 20))
        next_button = tk.Button(buttons_frame, text="Next", 
                                font=BODY, command=next_function)
        next_button.grid(row=0, column=1, padx=(20, 0))
        buttons_frame.grid(row=2, pady=(40, 20))
        problems_frame.grid()

    def get_start_frame(self):
        def confirm_function():
            start_frame.grid_remove()
            self.get_question_frame()
            self.media.play_sound("click_button")

        def back_function():
            start_frame.grid_remove()
            self.get_problems_frame()
            self.media.play_sound("click_button")

        start_frame = tk.Frame(self.root)
        self.root.bind("<Return>", lambda event: confirm_function())
        parameters_text = (f"Username: {self.username}\nOperation: "
                           f"{self.operation_name}\nDifficulty: "
                           f"{difficulty_dict[self.difficulty]}\nNumber "
                           f"of Problems: {self.problem_total}")
        prompt = tk.Label(start_frame, 
                          text="Check the following parameters:", 
                          font=HEADING)
        prompt.grid(row=0, pady=(0, 20))
        parameters_label = tk.Label(start_frame, text=parameters_text, 
                              font=BODY)
        parameters_label.grid(row=1, pady=(0, 20))
        button_frame = tk.Frame(start_frame)
        button_frame.grid(row=2)
        back_button = tk.Button(button_frame, text="Back", font=BODY, 
                                command=back_function)
        back_button.grid(row=0, column=0, padx=(0, 20), pady=(0, 40))
        confirm_button = tk.Button(button_frame, text="Confirm", 
                                   font=BODY, command=confirm_function)
        confirm_button.grid(row=0, column=1, padx=(20, 0), pady=(0, 40))
        start_frame.grid()

    def get_question_frame(self):
        def submit_function(solution):
            self.problem_counter += 1
            if self.problem_counter > self.problem_total:
                question_frame.grid_remove()
                self.elapsed_time = round(time.time() - self.start_time, 3)
                self.correct_ratio = (self.correct_answers / 
                                      self.problem_total)
                self.score = int(((self.difficulty * self.correct_ratio * 
                                   self.problem_total * 10) / 
                                   self.elapsed_time) * 100)
                self.get_end_frame()
            else:
                correct_response = self.check_answer(int(answer_box.get()), 
                                                    self.solution)
                question_num_label.config(
                    text=f"Q{self.problem_counter}.\nSolve the equation" 
                    " below:")
                self.equation, self.solution = self.generate_question()
                if correct_response:
                    feedback_label.config(text="Correct!")
                    self.media.play_sound("correct_answer")
                    self.correct_answers += 1
                else:
                    feedback_label.config(text="Incorrect.\nThe answer was "
                                        f"{solution}")
                    self.media.play_sound("incorrect_answer")
                answer_box.delete(0, tk.END)
                equation_label.config(text=self.equation)

        def update_timer():
            elapsed_seconds = round(time.time() - self.start_time, 1)
            elapsed_time.set(f"Elapsed Time: {elapsed_seconds}")
            self.root.after(100, update_timer)

        self.start_time = time.time()
        question_frame = tk.Frame(self.root)
        elapsed_time = tk.StringVar(self.root, "0.0")
        self.equation, self.solution = self.generate_question()
        self.root.bind("<Return>", lambda event: 
                       submit_function(self.solution))
        timer_label = tk.Label(question_frame, 
                               textvariable=elapsed_time, font=BODY)
        timer_label.grid(row=0, pady=(0, 2))
        question_num_label = tk.Label(question_frame, 
                                      text=f"Q{self.problem_counter+1}.\nSolve"
                                      " the equation below:", 
                                      font=HEADING)
        question_num_label.grid(row=1, pady=(0, 20))
        equation_label = tk.Label(question_frame, text=self.equation, 
                                  font=HEADING)
        equation_label.grid(row=2, pady=(0, 20))
        answer_box = tk.Entry(question_frame, font=BODY)
        answer_box.grid(row=3, pady=(0, 20))
        feedback_label = tk.Label(question_frame, text="", font=HEADING)
        feedback_label.grid(row=4, pady=(0, 20))
        submit_button = tk.Button(question_frame, text="Submit", font=BODY, 
                                  command=lambda: 
                                  submit_function(self.solution))
        submit_button.grid(row=5, pady=(40, 40))
        question_frame.grid()
        update_timer()
        answer_box.focus_set()

    def get_end_frame(self):
        def save_function():
            self.save_score()
            save_button.config(text="View Graph", command=self.view_graph)
            results_label.config(text="Leaderboard updated.")
            update_leaderboard()
            self.media.play_sound("click_button")

        def again_function():
            self.problem_counter = 0
            self.correct_answers = 0
            end_frame.grid_remove()
            self.get_username_frame()
            self.media.play_sound("click_button")

        def main_menu_function():
            end_frame.grid_remove()
            self.get_main_menu_frame()
            self.media.play_sound("click_button")

        def update_leaderboard():
            leaderboard = self.get_leaderboard()
            for row in leaderboard_view.get_children():
                leaderboard_view.delete(row)
            for index, row in leaderboard[:10].iterrows():
                leaderboard_view.insert("", "end", values=list(row))
        
        leaderboard = self.get_leaderboard()
        self.root.bind("<Return>", lambda event: None)
        end_frame = tk.Frame(self.root)
        buttons_frame = tk.Frame(end_frame)
        feedback_label = tk.Label(end_frame, text=f"{self.get_results()}," 
                                 f"{self.username}.", font=HEADING)
        feedback_label.grid(row=0, pady=(0, 20))
        leaderboard_view = ttk.Treeview(end_frame, 
                                        columns=leaderboard.columns.tolist(), 
                                        show="headings")
        for column in leaderboard.columns:
            leaderboard_view.column(column, width=60)
            leaderboard_view.heading(column, text=column)
        leaderboard_view.grid(row=1, pady=(0, 20))
        for index, row in leaderboard[:10].iterrows():
            leaderboard_view.insert("", "end", values=list(row))
        results_label = tk.Label(end_frame, 
                                 text=f"Your score was:\n{self.score}",
                                 font=HEADING)
        results_label.grid(row=2, pady=(0, 20))
        save_button = tk.Button(buttons_frame, text="Save Score", font=BODY,
                                     command=save_function)
        save_button.grid(row=0, column=0, padx=(0, 20))
        again_button = tk.Button(buttons_frame, text="Play Again", font=BODY, 
                                 command=again_function)
        again_button.grid(row=0, column=1, padx=(20, 20))
        main_menu_button = tk.Button(end_frame, text="Main Menu", 
                                     font=BODY, command=main_menu_function)
        buttons_frame.grid(row=3, pady=(0, 20))
        main_menu_button.grid(row=4, column=0, pady=(0, 20))
        end_frame.grid()
