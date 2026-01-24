board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]


def game_input(symbol):
    while True:

        row = int(input(f"Player {symbol}.Choose your row :"))
        colomn = int(input(f"Player {symbol}.Choose your colomn :"))
        if row < 0 or row > 2 or colomn < 0 or colomn > 2:
            print("Out of bounds!")
            continue
        if not board[row][colomn] == " ":
            print("Spot is taken.")
        else:
            board[row][colomn] = symbol
            for screen in board:
                print("  |  ".join(screen))
                print("--------------")
            break


def win():
    for r in range(3):
        if board[r][0] == board[r][1] == board[r][2] != " ":
            return True
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False


for turn in range(9):
    if turn % 2 == 0:
        present_symbol = "X"
    else:
        present_symbol = "O"

    game_input(present_symbol)

    if win():
        print(f"Congratulations! Player {present_symbol} wins!")
        break
else:
    print("It's a tie.")
