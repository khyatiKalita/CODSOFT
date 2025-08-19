import turtle
import math

# Game state
board = [[" " for _ in range(3)] for _ in range(3)]
cell_size = 100
offset = -150  # To center the board

def draw_board():
    turtle.clear()
    turtle.hideturtle()
    turtle.speed(0)
    turtle.pensize(3)
    # Draw grid
    for i in range(1, 3):
        # Vertical lines
        turtle.penup()
        turtle.goto(offset + i * cell_size, offset)
        turtle.pendown()
        turtle.goto(offset + i * cell_size, offset + 3 * cell_size)
        # Horizontal lines
        turtle.penup()
        turtle.goto(offset, offset + i * cell_size)
        turtle.pendown()
        turtle.goto(offset + 3 * cell_size, offset + i * cell_size)
    # Draw marks
    for i in range(3):
        for j in range(3):
            x = offset + j * cell_size + cell_size // 2
            y = offset + i * cell_size + cell_size // 2
            if board[i][j] == "X":
                draw_x(x, y)
            elif board[i][j] == "O":
                draw_o(x, y)
    turtle.update()

def draw_x(x, y):
    turtle.penup()
    turtle.goto(x - 30, y - 30)
    turtle.pendown()
    turtle.setheading(45)
    turtle.forward(60)
    turtle.penup()
    turtle.goto(x + 30, y - 30)
    turtle.pendown()
    turtle.setheading(135)
    turtle.forward(60)
    turtle.penup()

def draw_o(x, y):
    turtle.penup()
    turtle.goto(x, y - 30)
    turtle.pendown()
    turtle.setheading(0)
    turtle.circle(30)
    turtle.penup()

def check_winner(board, player):
    for i in range(3):
        if all([cell == player for cell in board[i]]):
            return True
        if all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]):
        return True
    if all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_full(board):
    return all([cell != " " for row in board for cell in row])

def get_available_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                moves.append((i, j))
    return moves

def minimax(board, depth, is_maximizing, alpha, beta):
    if check_winner(board, "O"):
        return 1
    if check_winner(board, "X"):
        return -1
    if is_full(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for (i, j) in get_available_moves(board):
            board[i][j] = "O"
            eval = minimax(board, depth + 1, False, alpha, beta)
            board[i][j] = " "
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for (i, j) in get_available_moves(board):
            board[i][j] = "X"
            eval = minimax(board, depth + 1, True, alpha, beta)
            board[i][j] = " "
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def ai_move():
    best_score = -math.inf
    move = None
    for (i, j) in get_available_moves(board):
        board[i][j] = "O"
        score = minimax(board, 0, False, -math.inf, math.inf)
        board[i][j] = " "
        if score > best_score:
            best_score = score
            move = (i, j)
    if move:
        board[move[0]][move[1]] = "O"

def click_handler(x, y):
    if check_winner(board, "X") or check_winner(board, "O") or is_full(board):
        return
    # Convert click to board indices
    col = int((x - offset) // cell_size)
    row = int((y - offset) // cell_size)
    if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
        board[row][col] = "X"
        draw_board()
        if check_winner(board, "X"):
            turtle.title("You win!")
            return
        if is_full(board):
            turtle.title("It's a draw!")
            return
        ai_move()
        draw_board()
        if check_winner(board, "O"):
            turtle.title("AI wins!")
        elif is_full(board):
            turtle.title("It's a draw!")

def main():
    turtle.tracer(0, 0)
    turtle.setup(width=400, height=400)
    turtle.title("Tic-Tac-Toe: You (X) vs AI (O)")
    draw_board()
    turtle.onscreenclick(click_handler)
    turtle.done()

if __name__ == "__main__":
    main()