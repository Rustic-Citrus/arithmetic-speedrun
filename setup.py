import operator
import os

def check_cwd() -> bool:
    """Checks to see if the current working directory is the 
    'arithmetic-speedrun' folder."""
    cwd = os.getcwd()
    if cwd[-19:] == "arithmetic-speedrun":
        return True
    else:
        return False

def introduction() -> str:
    """Start the script by displaying the README.md file."""
    with open("README.md", "r") as f:
        readme = f.readlines()
    intro = "".join(readme)
    return intro

def difficulty() -> int:
    """Asks the user for a difficulty level (1-6) and returns the user's 
    input."""
    with open("difficulty.txt", "r") as f:
        difficulty_settings = f.readlines()
    print("".join(difficulty_settings))
    user_setting = ""
    while (not isinstance(user_setting, int) or user_setting > 6 or 
        user_setting < 1):
        user_setting = int(input("Choose a difficulty setting:\n>: "))
        if not isinstance(user_setting, int):
            print("TypeError: difficulty argument should be an integer.")
        elif (user_setting > 6 or user_setting < 1):
            print("ValueError: difficulty should be between 1 and 6.")
    return user_setting

def problem_count() -> int:
    """Asks the user for a problem count (>=5) and returns the user's input."""
    problem_count = 0
    while problem_count < 5:
        try:
            problem_count = int(
                input("How many problems do you want to try?\n>: "))
            if problem_count < 5:
                print("ValueError: Must be equal to or greater than 5.")
        except ValueError:
            print("TypeError: Please type a number.")
    return problem_count

def operation() -> tuple:
    """Asks the user to choose an arithmetic operation and returns the user's 
    choice."""
    options = ["=== Operations ===\n", "1. Addition\n", "2. Subtraction\n",
                "3. Multiplication\n", "4. Division"]
    print("".join(options))
    operation = None
    while operation is None:
        try:
            choice = int(input(
            "Type the number of the operation you want to practice:\n>: "))
            if (choice >= 1) and (choice <= 4):
                match choice:
                    case 1:
                        operation = (operator.add, "+")
                    case 2:
                        operation = (operator.sub, "-")
                    case 3:
                        operation = (operator.mul, "*")
                    case 4:
                        operation = (operator.truediv, "/")
            else:
                raise ValueError
        except TypeError:
            print("TypeError: Choice must be a number.")
        except ValueError:
            print("ValueError: Choice must be between 1 and 4.")
    return operation
