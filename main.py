import random
import art

def lives_set():
    hardness = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if hardness == "easy":
        return 10
    elif hardness == "hard":
        return 5
    else:
        print("You did not type a valid choice.")
        lives_set()

def compare_numbers(guess, answer, lives):
    if guess == answer:
        print(f"You got it! The answer was {answer}.")
        return lives
    if guess < answer:
        print("Too low.\nGuess again.")
        return lives - 1
    else:
        print("Too High. \nGuess again.")
        return lives - 1

def play_game():
    print(art.logo)
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1,100)
    print(f"Pssst, the correct answer is {answer}.")
    lives = lives_set()
    guess = 0
    while lives > 0 and guess != answer:
        print(f"You have {lives} attempt(s) remaining to guess the number.")
        guess = int(input("Make a guess: "))
        lives = compare_numbers(guess, answer, lives)    
    if lives == 0:
        print("You've run out of guesses, you lose.")
    

play_game()
