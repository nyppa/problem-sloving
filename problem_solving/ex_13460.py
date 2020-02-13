# 구슬 탈출 2 (문제 13460번)
def escape_bead(try_num, board, red_ball, blue_ball, hole):
    if try_num > 10:
        return -1
    try_case = [try_num]*4
    red_ball_row, red_ball_col = red_ball # 빨간 공의 행, 열
    blue_ball_row, blue_ball_col = blue_ball # 파란 공의 행, 열
    red_obstacle = []
    blue_obstacle = []
    red_obstacle.append([red_ball_row, board[red_ball_row].index('#', red_ball_col+1)]) # 빨간 공의 오른쪽에서 가장 가까운 장애물의 위치
    blue_obstacle.append([blue_ball_row, board[blue_ball_row].index('#', blue_ball_col+1)]) #파란 공의 오른쪽에서 가장 가까운 장애물의 위치
    red_obstacle.append([red_ball_row, len(board[0])-list(reversed(board[red_ball_row])).index('#', len(board[0])-red_ball_col-1)-1]) # 왼쪽 장애물
    blue_obstacle.append([blue_ball_row, len(board[0])-list(reversed(board[blue_ball_row])).index('#', len(board[0])-blue_ball_col-1)-1])

    for i in range(red_ball_row-1, -1, -1): # 위쪽 장애물
        if board[i][red_ball_col] == '#':
            red_obstacle.append([i, red_ball_col])
            break
    for i in range(blue_ball_row-1, -1, -1):
        if board[i][blue_ball_col] == '#':
            blue_obstacle.append([i, blue_ball_col])
            break
    for i in range(red_ball_row+1, len(board)): #아래쪽
        if board[i][red_ball_col] == '#':
            red_obstacle.append([i, red_ball_col])
            break
    for i in range(blue_ball_row+1, len(board)):
        if board[i][blue_ball_col] == '#':
            blue_obstacle.append([i, blue_ball_col])
            break
    if 'O' in board[blue_ball_row][blue_ball_col:blue_obstacle[0][1]]: # 오른쪽에 구멍이 있다면 실패
        try_case[0] = -1
    elif 'O' in board[red_ball_row][red_ball_col:red_obstacle[0][1]]: # 성공한 경우
        try_case[0] += 1
    else:
        if blue_obstacle[0] == red_obstacle[0] : # 장애물의 위치가 같을 때
            if blue_ball_col > red_ball_col:
                red_ball_col = red_obstacle[0][1]-2
                blue_ball_col = blue_obstacle[0][1]-1
            else:
                red_ball_col = red_obstacle[0][1]-1
                blue_ball_col = blue_obstacle[0][1]-2
        else:
            red_ball_col = red_obstacle[0][1]-1
            blue_ball_col = blue_obstacle[0][1]-1
        try_case[0] = escape_bead(try_case[0]+1, board, [red_ball_row, red_ball_col], [blue_ball_row, blue_ball_col], hole)

    red_ball_row, red_ball_col = red_ball # 빨간 공의 행, 열
    blue_ball_row, blue_ball_col = blue_ball # 파란 공의 행, 열
    if 'O' in board[blue_ball_row][blue_ball_col:blue_obstacle[1][1]:-1]: # 왼쪽에 구멍이 있다면 실패
        try_case[1] = -1
    elif 'O' in board[red_ball_row][red_ball_col:red_obstacle[1][1]:-1]: # 성공한 경우
        try_case[1] += 1
    else:
        if blue_obstacle[1] == red_obstacle[1] : # 장애물의 위치가 같을 때
            if blue_ball_col < red_ball_col:
                red_ball_col = red_obstacle[1][1]+2
                blue_ball_col = blue_obstacle[1][1]+1
            else:
                red_ball_col = red_obstacle[1][1]+1
                blue_ball_col = blue_obstacle[1][1]+2
        else:
            red_ball_col = red_obstacle[1][1]+1
            blue_ball_col = blue_obstacle[1][1]+1
        try_case[1] = escape_bead(try_case[1]+1, board, [red_ball_row, red_ball_col], [blue_ball_row, blue_ball_col], hole)

    red_ball_row, red_ball_col = red_ball # 빨간 공의 행, 열
    blue_ball_row, blue_ball_col = blue_ball # 파란 공의 행, 열
    if hole[1] == blue_ball_col and blue_obstacle[2][0] < hole[0] < blue_ball_row: # 위쪽에 구멍이 있다면 실패
        try_case[2] = -1
    elif hole[1] == red_ball_col and red_obstacle[2][0] < hole[0] < red_ball_row: # 성공한 경우
        try_case[2] += 1
    else :
        if blue_obstacle[2] == red_obstacle[2] : # 장애물의 위치가 같을 때
            if blue_ball_row < red_ball_row:
                red_ball_row = red_obstacle[2][0]+2
                blue_ball_row = blue_obstacle[2][0]+1
            else :
                red_ball_row = red_obstacle[2][0]+1
                blue_ball_row = blue_obstacle[2][0]+2
        else:
            red_ball_row = red_obstacle[2][0]+1
            blue_ball_row = blue_obstacle[2][0]+1
        try_case[2] = escape_bead(try_case[2]+1, board, [red_ball_row, red_ball_col], [blue_ball_row, blue_ball_col], hole)

    red_ball_row, red_ball_col = red_ball # 빨간 공의 행, 열
    blue_ball_row, blue_ball_col = blue_ball # 파란 공의 행, 열
    if hole[1] == blue_ball_col and blue_ball_row < hole[0] < blue_obstacle[3][0]: # 아래쪽에 구멍이 있다면 실패
        try_case[3] = -1
    elif hole[1] == red_ball_col and red_ball_row < hole[0] < red_obstacle[3][0]: # 성공한 경우
        try_case[3] += 1
    else :
        if blue_obstacle[3] == red_obstacle[3]: # 장애물의 위치가 같을 때
            if blue_ball_row > red_ball_row:
                red_ball_row = red_obstacle[3][0]-2
                blue_ball_row = blue_obstacle[3][0]-1
            else :
                red_ball_row = red_obstacle[3][0]-1
                blue_ball_row = blue_obstacle[3][0]-2
        else:
            red_ball_row = red_obstacle[3][0]-1
            blue_ball_row = blue_obstacle[3][0]-1
        try_case[3] = escape_bead(try_case[3]+1, board, [red_ball_row, red_ball_col], [blue_ball_row, blue_ball_col], hole)

    try_min = 11
    for i in range(4):
        if try_case[i] < try_min and try_case[i] != -1:
            try_min = try_case[i]
    if try_min == 11:
        try_min = -1
    return try_min

M, N = map(int, input().split()) # M, N 은 행과 열
board = []
for m in range(M):
    board.append(list(input()))
    if board[m].count('R') == 1:
        red_ball = [m, board[m].index('R')]
    if board[m].count('B') == 1:
        blue_ball = [m, board[m].index('B')]
    if board[m].count('O') == 1:
        hole_loc = [m, board[m].index('O')]

try_num = 0
try_num = escape_bead(try_num, board, red_ball, blue_ball, hole_loc)
print(try_num)