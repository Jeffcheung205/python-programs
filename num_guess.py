import random as random

ran_num = random.randint(1, 100)
min_num = 1
max_num = 100

while True:
    print(f"Current range: {min_num}-{max_num}")
    guess = input(f"Guess a number between {min_num} and {max_num}: ")

    try:
        guess = int(guess)

        # Check within current range
        if guess < min_num or guess > max_num:
            print(f"Please guess a number within the range of {min_num} to {max_num}.")
            continue

        # Update range after the guess
        if guess < ran_num:
            # Guess is too low: new range is guess-high
            min_num = guess
            print(f"{min_num}-{max_num}")
        elif guess > ran_num:
            # Guess is too high: new range is low-guess
            max_num = guess
            print(f"{min_num}-{max_num}")
        else:
            print("Congratulations! You've guessed the correct number!")
            break

    except ValueError:
        print("Invalid input. Please enter a valid integer.")
