import random

top_of_range = input("Type a number: ")

guesses = 0

try:
    top_of_range_int = int(top_of_range)
    if top_of_range_int <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
except Exception:
    print("Please type a number next time.")
    quit()

random_number = random.randint(0, top_of_range_int)

while True:
    user_guess = input("Make a guess: ")
    try:
        user_guess_int = int(user_guess)
        guesses += 1
        if user_guess_int > random_number:
            print("You were above the number.")
        elif user_guess_int < random_number:
            print("You were below the number.")
        if user_guess_int == random_number:
            print("You got it!")
            print(f"You got it in {guesses} guesses.")
            break
    except Exception:
        print("Please type a number next time.")
        continue
