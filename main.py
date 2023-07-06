import problems
import time

# Start the script by displaying the README.md file.
with open("README.md", "r") as f:
    readme = f.readlines()
print("".join(readme))

# Initiate a loop that continues relieves consent to continue playing.
play_again = "Y"
while play_again.upper() == "Y":

    # Initiate a counter that tracks the number of problems the user has seen.
    counter = 0

    # Initiate a counter, score, that tracks the number of correct answers the 
    # user has provided.
    score = 0

    # Set the number of problems to be shown per round.
    problem_count = 5

    # Ask the user what difficulty they want to play on.
    difficulty = problems.get_difficulty()

    # Initiate a timer and and start the round.
    start_time = time.time()
    while counter < problem_count:
        for n in range(problem_count):
            problem = problems.get_problem(difficulty)
            correct_answer = problems.get_input(problem)
            if correct_answer:
                score += 1
                problems.correct_answer_sound.play()
            else:
                problems.incorrect_answer_sound.play()
            counter += 1

    # Calculate the total time the user took to complete the problems.
    elapsed_time = time.time() - start_time

    # Play a different sound depending on whether the user got a high or low 
    # score.
    if score > 3:
        problems.high_score_sound.play()
    else:
        problems.low_score_sound.play()

    # Fetch the leaderboard and print it to the console.
    problems.get_leaderboard()

    # Print the user's score and time to the console, and ask them if they 
    # want to save it. If they press the Y key, request their username and 
    # save it to leaderboard.csv.       
    print(f"\rElapsed time: {elapsed_time:.2f} seconds")
    print(f"You scored {score} out of 5.")
    save_score = input("Would you like to save your score? (press Y).\n" 
                        + ">: ")
    if save_score.upper() == "Y":
        username = input("Choose a username.\n>: ")
        problems.set_leaderboard(username, score, difficulty, elapsed_time)

        # Ask the user if they would like to see how much progress they have 
        # made.
        see_progress = input("Would you like to see how your score has " + 
                             "changed over time? (press Y)\n>: ")
        if see_progress.upper() == "Y":
            problems.get_progress(username, difficulty)

    # Ask the user if they want to continue playing. If they press the Y key, 
    # restart the game loop.
    play_again = input("Would you like to play again? (press Y)\n>: ")

# If the user decides not to continue playing, print a friendly goodbye to the 
# console.
print("Thanks for playing!")
