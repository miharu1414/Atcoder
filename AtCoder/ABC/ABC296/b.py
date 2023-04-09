def find_piece(board):
    for i in range(8):
        for j in range(8):
            if board[i][j] == "*":
                return chr(97 + j) + str(8-i )
s = [input() for i in range(8)]
print(find_piece(s))