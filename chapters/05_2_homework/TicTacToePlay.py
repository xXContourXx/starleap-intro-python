#I did not make this, the code was generated using ChatGPT. I just wanted to play around with python!

import math, random

def print_board(board):
    print("\n")
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("---------")
    print("\n")

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def is_moves_left(board):
    return any(" " in row for row in board)

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "O":
        return 10 - depth
    if winner == "X":
        return depth - 10
    if not is_moves_left(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(best_score, score)
        return best_score

def best_move(board, difficulty):
    best_score = -math.inf
    moves = []

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                moves.append(((i, j), score))
                if score > best_score:
                    best_score = score

    # difficulty controls how often AI plays imperfectly
    if difficulty == "easy":
        # pick random move 70% of the time
        if random.random() < 0.7:
            return random.choice([m[0] for m in moves])
    elif difficulty == "normal":
        # pick random move 30% of the time
        if random.random() < 0.3:
            return random.choice([m[0] for m in moves])

    # otherwise, pick best move
    best_moves = [m[0] for m in moves if m[1] == best_score]
    return random.choice(best_moves)

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe!")
    print("You are X, the AI is O.")

    difficulty = ""
    while difficulty not in ["easy", "normal", "hard"]:
        difficulty = input("Choose difficulty (easy / normal / hard): ").lower().strip()

    print_board(board)

    while True:
        # Player move
        while True:
            try:
                move = input("Enter your move (row and column: 1 2): ").split()
                if len(move) != 2:
                    raise ValueError
                row, col = map(int, move)
                if not (1 <= row <= 3 and 1 <= col <= 3):
                    raise ValueError
                if board[row - 1][col - 1] != " ":
                    print("That spot is taken! Try again.")
                    continue
                break
            except ValueError:
                print("Invalid input! Use format: row col (e.g., 1 2)")
        board[row - 1][col - 1] = "X"
        print_board(board)

        if check_winner(board) == "X":
            print("You win!")
            break
        if not is_moves_left(board):
            print("It's a draw!")
            break

        print("AI is thinking...")
        ai_row, ai_col = best_move(board, difficulty)
        board[ai_row][ai_col] = "O"
        print_board(board)

        if check_winner(board) == "O":
            print("AI wins!")
            break
        if not is_moves_left(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
