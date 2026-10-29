
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False


# Initialize the game
board = [[" " for _ in range(3)] for _ in range(3)]
player = "X"

for turn in range(9):
    print("\nCurrent Board:")
    print_board(board)
    print(f"Player {player}'s turn")

    try:
        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        continue

    # Validate row and column
    if row not in range(3) or col not in range(3):
        print("Invalid position! Enter values between 0 and 2.")
        continue

    # Check if the cell is empty
    if board[row][col] != " ":
        print("Cell already occupied! Try again.")
        continue

    # Place the player's mark
    board[row][col] = player

    # Check for a winner
    if check_winner(board):
        print("\nFinal Board:")
        print_board(board)
        print(f"Player {player} wins!")
        break

    # Switch players
    player = "O" if player == "X" else "X"

else:
    print("\nFinal Board:")
    print_board(board)
    print("Game Draw!")
