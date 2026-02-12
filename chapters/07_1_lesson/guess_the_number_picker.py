# Number Guessing Game - Picker
# The program thinks of a number between 1 and 100 and the user tries to guess it.
# The program should tell the user if the guess is too high or too low.
# The program should also tell the user how many guesses it took to guess the number.
import random

MIN_NUMBER = 1
MAX_NUMBER = 100

def get_valid_guess():
    while True:
      guess_text = input('Enter your guess')
      try:
          guess = int(guess_text)
          if guess > MAX_NUMBER or guess < MIN_NUMBER:
              raise ValueError()
          return guess
      except:
          print('Hey, put in a valid guess dummie')
    

    pass

def play_picker():
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    #print(f"Computer picked {number}.")
    print(f"I have picked a number between {MIN_NUMBER} and {MAX_NUMBER}.")
    while True:
        guess = get_valid_guess()
        if guess == number:
            print("Guessed right, you rock!")
            break
        elif guess > number:
            print("incorrect, guess too high")
        
        else:
            print('incorrect, guess too low')

    pass

    

def main():
    print('=' * 60)
    print()
    print("Welcome to the Number Guessing Game!")
    print()
    while True:
        guess_count = play_picker()
        answer = input("Do you want to play again? (y/n) ").lower()
        if answer != "y":
            print("Thanks for playing!")

            break

if __name__ == "__main__":
    main()