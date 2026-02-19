# Number Guessing Game - Guesser
# The user thinks of a number between 1 and 100 and the program tries to guess it.
# The user should tell the program if the guess is too high, too low, or correct.
# The program should tell the user how many guesses it took to guess the number.

import random

MIN_NUMBER = 1
MAX_NUMBER =100


def get_number_feedback():
    answer = ''
    while answer != 'h' and answer !='l' and answer !='c':
     answer = input('If guess is too high, enter H. If it is too low, enter L. If it is correct enter C.')
    return answer



def get_number():
    return(MIN_NUMBER + MAX_NUMBER) // 2


def play_guesser():
    global MIN_NUMBER
    global MAX_NUMBER
    print('-' * 60)
    print()
    print(f"Think of a number between 1 and 100 (inclusive).")
    input("Press Enter when you have thought of a number.")
    guess_count = 0
    while True:
        guess_count += 1
        guess = get_number()
        print(F'Is it {guess}?')
        #computer makes a guess
        feedback = get_number_feedback()
        #ask guess feedback - high low or corrcect
        if feedback == 'c':
            print(f"hehe I guessed your number in {guess_count} guesses")
            return guess_count
        elif feedback == 'h':
            MAX_NUMBER = guess -1
        elif feedback == 'l':
            MIN_NUMBER = guess + 1
        #if correct kill function
        #if not guess again
    

def main():
    print('-' * 60)
    print()
    print("Welcome to the Number Guessing Game!")
    print()
    while True:
        guess_count = play_guesser()
        answer = input("Do you want to play again? (y/n) ").lower()
        if answer != "y":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()