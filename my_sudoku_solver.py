board1 = [
    [1,0,0,0,0,0,0,0,0],
    [5,9,8,3,0,4,6,2,0],
    [7,6,4,1,0,0,3,8,0],
    [8,0,1,2,0,6,4,0,0],
    [0,4,0,0,0,1,2,0,0],
    [0,5,6,7,0,0,0,0,0],
    [4,2,0,0,5,8,0,3,0],
    [0,0,0,0,3,2,8,7,6],
    [0,0,0,0,0,0,0,0,0]
]

def whole_board(board1):
    for i in range(len(board1)):
        if i % 3 == 0 and i != 0:
            print(" ")
        for j in range(len(board1[0])):
            if j % 3 == 0 and j != 0:
                print(" ", end="")
            if j == 8:
                print(board1[i][j])
            else:
                print(str(board1[i][j]) + " ", end="")

def finds_empty_boxes(board1):
    for i in range(len(board1)):
        for j in range(len(board1[0])):
            if board1[i][j] == 0:
                return (i, j)
    return None

def solve(board1):
    find = finds_empty_boxes(board1)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1,10):
        if validate(board1, i, (row, col)):
            board1[row][col] = i
            if solve(board1):
                return True
            board1[row][col] = 0
    return False

def validate(board1, num, pos):
    for i in range(len(board1[0])):
        if board1[pos[0]][i] == num and pos[1] != i:
            return False
    for i in range(len(board1)):
        if board1[i][pos[1]] == num and pos[0] != i:
            return False
    board1x_x = pos[1] // 3
    board1x_y = pos[0] // 3
    for i in range(board1x_y*3, board1x_y*3 + 3):
        for j in range(board1x_x * 3, board1x_x*3 + 3):
            if board1[i][j] == num and (i,j) != pos:
                return False
    return True

def whole_board(board1):
    for i in range(len(board1)):
        if i % 3 == 0 and i != 0:
            print(" ")
        for j in range(len(board1[0])):
            if j % 3 == 0 and j != 0:
                print("  ", end="")
            if j == 8:
                print(board1[i][j])
            else:
                print(str(board1[i][j]) + " ", end="")
print()
print("Given board")
print()
whole_board(board1)
solve(board1)
print()
print("Solved")
print()
whole_board(board1)
