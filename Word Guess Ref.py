answer = "apple"

print("Type of fruit with five letter and red in color")

while True:
    guess = input("Your guess: ")

    # case-insensitive comparison
    if guess.lower() == answer.lower():   # convert both to lowercase [web:8]
        print("Bingo!")
        break
    else:
        print("Wrong guess, try again!")
