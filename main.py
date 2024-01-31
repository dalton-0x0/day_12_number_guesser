from random import randint

from art import logo, logo_win

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# Function to check user's guess against actual answer.
def check_answer(guess: int, answer: int, turns: int):
    """
    Compares the guess to the answer and prints feedback based on the comparison.
    Reduces the number of turns by 1 if the guess is incorrect.
    Prints a winning message if the guess is correct.

    :param guess: The number guessed by the player.
    :param answer: The correct number to be guessed.
    :param turns: The current number of turns remaining before this guess.

    :return: The updated number of turns remaining after this guess.
             If the guess is correct, the turns are not reduced.
    """
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(logo_win)
        print(f"You got it! The answer was {answer}.")
        return turns


# Make function to set difficulty.
def set_difficulty():
    """
    Sets the difficulty level of the game
    :return:
    """
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    """
    The main game play function
    :return:
    """
    print(logo)
    # Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)

    # for debbuging, you can see the answer
    # print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()
    # Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        # Let the user guess a number.
        guess = int(input("Make a guess: "))

        # Track the number of turns and reduce by 1 if they get it wrong.
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")


game()
