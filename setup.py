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
