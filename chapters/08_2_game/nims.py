
def player_answer():
    MIN_NUMBER = 1
    MAX_NUMBER = 5
    print('Please enter a number between')
    while True:
        answer = int(input(''))
        if answer > MAX_NUMBER or answer < MIN_NUMBER:
            print(f"error, please enter a number between {MIN_NUMBER} and {MAX_NUMBER}")
        else:
           return answer
        
player_answer()
    
    








#def play_nims(pile, max_stones):
    #while pile >=0:

    