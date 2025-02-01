import random

def print_board(board):
    print("\n    1   |   2   |   3  ")
    print(f"   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}  ")
    print("--------+-------+--------")
    print("    4   |   5   |   6  ")
    print(f"   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}  ")
    print("--------+-------+--------")
    print("    7   |   8   |   9  ")
    print(f"   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}  \n")

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):
            return True
        if all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def is_draw(board):
    return all([cell != " " for row in board for cell in row])

def get_empty_positions(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == " ":
                return row, col
            else:
                print("Cell is already occupied. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Enter a number between 1 and 9.")

def computer_move(board, difficulty):
    print("Computer is thinking...")
    if difficulty == "easy":
        return random.choice(get_empty_positions(board))  # Random move for easy
    elif difficulty == "medium":
        # Check for winning move or blocking move
        for player in ["O", "X"]:
            for i in range(3):
                for j in range(3):
                    if board[i][j] == " ":
                        board[i][j] = player
                        if check_winner(board, player):
                            board[i][j] = " "
                            return i, j
                        board[i][j] = " "
        return random.choice(get_empty_positions(board))  # Random move if no immediate win/block
    elif difficulty == "hard":
        # Minimax algorithm (implementation omitted for brevity)
        # ...
        return random.choice(get_empty_positions(board)) # random move for now

def tic_tac_toe():
    while True:
        print("\n==============================")
        print("     Welcome to Tic Tac Toe    ")
        print("==============================\n")

        mode = input("Choose mode:\n1. User vs User\n2. User vs Computer\nEnter 1 or 2: ")
        while mode not in ["1", "2"]:
            print("Invalid input. Please choose 1 or 2.")
            mode = input("Enter 1 or 2: ")

        if mode == "2":
            difficulty = input("Choose difficulty:\n1. Easy\n2. Medium\n3. Hard\nEnter 1, 2 or 3: ").lower()
            while difficulty not in ["1", "2", "3", "easy", "medium", "hard"]:
                print("Invalid input. Please choose 1, 2 or 3.")
                difficulty = input("Enter 1, 2 or 3: ").lower()
            if difficulty in ["1", "easy"]:
                difficulty = "easy"
            elif difficulty in ["2", "medium"]:
                difficulty = "medium"
            else:
                difficulty = "hard"

        board = [[" " for _ in range(3)] for _ in range(3)]
        player1 = "X"
        player2 = "O"
        current_player = player1

        while True:
            print_board(board)
            print(f"{current_player}'s turn.\n")

            if mode == "1" or (mode == "2" and current_player == player1):
                row, col = player_move(board)
            else:
                row, col = computer_move(board, difficulty)

            board[row][col] = current_player

            if check_winner(board, current_player):
                print_board(board)
                print(f"Congratulations! {current_player} wins the game!\n")
                break

            if is_draw(board):
                print_board(board)
                print("It's a draw! Well played both!\n")
                break

            current_player = player2 if current_player == player1 else player1

        play_again = input("Do you want to play another game? (yes/no): ").lower()
        if play_again != "yes":
            print("Thank you for playing Tic Tac Toe! Goodbye!")
            break

if __name__ == "__main__":
    tic_tac_toe()