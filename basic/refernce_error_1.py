board = [["-"] * 3] * 3
board[1][0] = "X"

for row in board:
    print(f"{row[0]} {row[1]} {row[2]}")