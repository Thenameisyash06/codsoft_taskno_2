import math

# Initialize the game board
def initialize_board():
    return [[' ' for i in range(3)] for i in range(3)]

# Print the board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Check for available moves
def get_available_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                moves.append((i, j))
    return moves

# Check if the game is over
def is_game_over(board):
    return check_winner(board, 'X') or check_winner(board, 'O') or not get_available_moves(board)

# Check for a winner
def check_winner(board, player):
    # Check rows
    for row in board:
        if all([cell == player for cell in row]):
            return True

    # Check columns
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    # Check diagonals
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    if check_winner(board, 'X'):
        return -1
    if check_winner(board, 'O'):
        return 1
    if not get_available_moves(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in get_available_moves(board):
            board[move[0]][move[1]] = 'O'
            score = minimax(board, depth + 1, False)
            board[move[0]][move[1]] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in get_available_moves(board):
            board[move[0]][move[1]] = 'X'
            score = minimax(board, depth + 1, True)
            board[move[0]][move[1]] = ' '
            best_score = min(score, best_score)
        return best_score

# Find the best move
def find_best_move(board):
    best_move = None
    best_score = -math.inf
    for move in get_available_moves(board):
        board[move[0]][move[1]] = 'O'
        score = minimax(board, 0, False)
        board[move[0]][move[1]] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

# Main game loop
def main():
    board = initialize_board()
    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while not is_game_over(board):
        # Player move
        player_move = input("Enter your move (row and column): ").split()
        row, col = int(player_move[0]), int(player_move[1])
        if board[row][col] == ' ':
            board[row][col] = 'X'
        else:
            print("Invalid move! Try again.")
            continue

        if is_game_over(board):
            break

        # Computer move
        computer_move = find_best_move(board)
        if computer_move:
            board[computer_move[0]][computer_move[1]] = 'O'
        print_board(board)

    if check_winner(board, 'X'):
        print("Congratulations! You win!")
    elif check_winner(board, 'O'):
        print("You lose! The computer wins.")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()
