import random
from art import logo

print(logo)
print(f"Welcome to the Number Guessing Game!")
print(f"------------------------------------")
print(f"I'm thinking of a number between 1 and 100.")

selected_number = random.choice(range(1, 101))
print(f"Selected number is {selected_number}")


difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty_level == "hard":
    attempt_count = 5
elif difficulty_level == "easy":
    attempt_count = 10

print(f"You have {attempt_count} attemps remaning to guess the number.")

while True:   
    guess = int(input("Make a guess: "))
    if guess > selected_number:
        attempt_count -= 1
        print("Too high.")
        print("Guess again")
        print(f"You have {attempt_count} attempts remaining to guess the number.")
    elif guess < selected_number:
        attempt_count -= 1
        print("Too low.")
        print("Guess again")
        print(f"You have {attempt_count} attempts remaining to guess the number.")
    else:
        print(f"That's it. The selected number is {selected_number}. You win.")
        break

    if attempt_count == 0:
        print(f"You've run out of guesses, you lose.")
        break