def introduction() -> str:
    """Start the script by displaying the README.md file."""
    with open("README.md", "r") as f:
        readme = f.readlines()
    intro = "".join(readme)
    return intro

def difficulty() -> int:
    """Reads the difficulty settings to the user and requests an integer 
    choice for difficulty, ranging from 1 to 6. If the user enters a valid 
    integer, it is returned with this function."""
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
