# 주사위 굴리기 (14499번 문제)
N, M, x, y, K = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(N)]
command_list = list(map(int, input().split()))
dice = [0] * 6
lower_surface = 5
east_surface = 2
south_surface = 4
for move_dir in command_list:
    if move_dir == 1: # 동쪽
        if(0 <= x < N and 0 <= y + 1 < M) == False:
            continue
        y += 1
        temp = east_surface
        east_surface = lower_surface
        lower_surface = 5 - temp

    elif move_dir == 2: # 서쪽
        if (0 <= x < N and 0 <= y - 1 < M) == False:
            continue
        y -= 1
        temp = lower_surface
        lower_surface = east_surface
        east_surface = 5 - temp
    elif move_dir == 3: # 북쪽
        if (0 <= x - 1 < N and 0 <= y < M) == False:
            continue
        x -= 1
        temp = south_surface
        south_surface = 5 - lower_surface
        lower_surface = temp
    else: # 남쪽
        if (0 <= x + 1 < N and 0 <= y < M) == False:
            continue
        x += 1
        temp = south_surface
        south_surface = lower_surface
        lower_surface = 5 - temp
    if grid[x][y] == 0:
        grid[x][y] = dice[lower_surface]
    else:
        dice[lower_surface] = grid[x][y]
        grid[x][y] = 0
    print(dice[5-lower_surface])