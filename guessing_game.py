import random

def guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("I'm thinking of a number between 1 and 100. Can you guess it?")
    
    while True:
        guess = int(input("Your guess: "))
        attempts += 1
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Correct! You got it in {attempts} guesses!")
            break


guessing_game()