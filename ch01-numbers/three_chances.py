import random

def guessing_game():
    """
    Chooses a random integer between 0 and 100 (inclusive).
    Aks a user for guess the number.
    Feedback is given to the user about whether too  high,
    too low, or just right.
    the program exists when the user gets it right.
    And you only get three chances!
    """
    chances = 0
    target = random.randint(0, 100)
    while chances < 3:
        try:
            guess = int(input("Guess an integer between 0 and 100 inclusive: "))
            chances += 1
        except ValueError as ve:
            print(f"an error occurred: {ve} Please enter an integer!")
            continue
        if guess == target:
            print("Just right!")
            break
        elif guess < target:
            print("Too low!")
        else:
            print("Too High!")
    print(f"You failed to guess after {chances} attempts!")


if __name__ == "__main__":
    guessing_game()



