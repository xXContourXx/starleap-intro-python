import os

def rock_paper_scissors():

    player1 = input('Player 1, choose rock, paper, or scissors: ').lower()
    while player1 not in ['rock', 'paper', 'scissors']:
        print("Invalid choice! You must choose 'rock', 'paper', or 'scissors'.")
        player1 = input('Player 1, choose rock, paper, or scissors: ').lower()
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    player2 = input('Player 2, choose rock, paper, or scissors: ').lower()
    while player2 not in ['rock', 'paper', 'scissors']:
        print(" Invalid choice! You must choose 'rock', 'paper', or 'scissors'.")
        player2 = input('Player 2, choose rock, paper, or scissors: ').lower()
    
    if (player1 == 'rock' and player2 == 'scissors'):
        print('player1 wins')
    elif (player1 == 'paper' and player2 == 'rock'):
        print('player1 wins')
    elif (player1 == 'scissors' and player2 == 'paper'):
        print('player1 wins')
    elif (player1 == player2):
        print('tie')
    else:
        print('player2 wins')

rock_paper_scissors()
