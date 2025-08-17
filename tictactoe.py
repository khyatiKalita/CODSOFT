import os

def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nTic-Tac-Toe Board (You are X, AI is O):\n")
    for i in range(3):
        row = []
        for j in range(3):
            idx = i * 3 + j
            cell = board[idx] if board[idx] != " " else str(idx + 1)
            row.append(cell)
        print(" " + " | ".join(row))
        if i < 2:
            print("---+---+---")
    print("\n")

import random

def check_winner(board, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8], # rows
        [0,3,6], [1,4,7], [2,5,8], # columns
        [0,4,8], [2,4,6]           # diagonals
    ]
    for cond in win_conditions:
        if all(board[i] == player for i in cond):
            return True
    return False

def is_draw(board):
    return all(cell != " " for cell in board)

def minimax(board, depth, is_maximizing):
    if check_winner(board, "O"):
        return 1
    if check_winner(board, "X"):
        return -1
    if is_draw(board):
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

def ai_move(board):
    best_score = -float("inf")
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

if _name_ == "_main_":
    board = [" "] * 9
    current_player = "X"
    while True:
        print_board(board)
        if current_player == "X":
            try:
                move = int(input("Enter your move (1-9): ")) - 1
                if move < 0 or move > 8 or board[move] != " ":
                    print("Invalid move. Try again.")
                    continue
                board[move] = "X"
            except ValueError:
                print("Please enter a valid number.")
                continue
        else:
            move = ai_move(board)
            if move is not None:
                board[move] = "O"
        if check_winner(board, current_player):
            print_board(board)
            print(f"{'You win!' if current_player == 'X' else 'AI wins!'}")
            break
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        current_player = "O" if current_player == "X" else "X"