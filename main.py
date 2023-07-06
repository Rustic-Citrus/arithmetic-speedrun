import problems
import time

try:
    play_again = "Y"
    while play_again.upper() == "Y":
        counter = 0
        score = 0
        problem_count = 5
        difficulty = problems.get_difficulty()
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
        elapsed_time = time.time() - start_time
        if score > 3:
            problems.high_score_sound.play()
        else:
            problems.low_score_sound.play()
        problems.get_leaderboard()        
        print(f"\rElapsed time: {elapsed_time:.2f} seconds")
        print(f"You scored {score} out of 5.")
        save_score = input("Would you like to save your score? (press Y).\n" 
                           + ">: ")
        if save_score.upper() == "Y":
            username = input("Choose a username.\n>: ")
            problems.set_leaderboard(username, score, difficulty, elapsed_time)
        play_again = input("Would you like to play again? (press Y)\n>: ")
    print("Thanks for playing!")
except OSError:
    pass