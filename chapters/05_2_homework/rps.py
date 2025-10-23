def rock_paper_scissors():

    player1=input('Choose rock, paper, or scissors:')

    player2=input('Choose rock, paper, or scissors:')
    
    if (player1== 'rock' and player2== 'scissors'):
        print('player1 wins')
    elif (player1== 'paper' and player2== 'rock'):
         print('player1 wins')
    elif (player1== 'scissors' and player2== 'paper'):
         print('player1 wins')
    elif (player1== player2):
         print('tie')
        
    else:
        print('player2 wins')

rock_paper_scissors()




    
