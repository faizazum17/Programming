#write a function which will return true if the king is in check, and false if he isn't.
def check(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == "K":
                king = (i, j)
            if board[i][j] == "Q":
                queen = (i, j) 
    #check if queen is in the same row
    if king[0] == queen[0]:
        return True
    #check if queen is in the same column
    elif king[1] == queen[1]:
        return True
    #check if queen is in the same diagonal
    elif abs(king[0] - queen[0]) == abs(king[1] - queen[1]):
        return True
    else:
        return False
    
print(check([
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", "Q", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", "K", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "]
    ])) #False

print(check([
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", "Q", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", "K", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", "Q", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", "Q", " ", " "]
    ])) #True

print(check([
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", "Q", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", "K", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", "Q", " "],
    [" ", " ", " ", "Q", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", "Q", " ", " "]
    ])) #True

