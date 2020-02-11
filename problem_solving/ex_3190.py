# 뱀 (문제 3190번)
N = int(input()) # 보드의 크기
K = int(input()) # 사과의 개수

apple_loc = []
end_time = 0 # 게임 진행 시간
live = True # 게임 중이면 True, 끝났으면 False
for k in range(K): # 사과 위치 입력
    apple_loc.append([])
    apple_loc[k] = list(map(int, input().split()))
L = int(input()) # 방향 변환 횟수
direction_info = [] # 방향 정보 리스트
current_dir = 1 # 초기 진행 방향은 오른쪽(1), 위(0), 아래(2), 왼쪽(3)
for l in range(L): # 방향 변환 정보 입력
    direction_info.append([])
    direction_info[l] = input().split()
    direction_info[l][0] = int(direction_info[l][0])
snake = [[1, 1]] # 뱀의 위치 snake[0]이 머리의 위치
while live == True:
    if current_dir == 1: # 진행 방향으로 머리 한 칸 이동
        snake.insert(0, [snake[0][0], snake[0][1]+1])
    if current_dir == 3:
        snake.insert(0, [snake[0][0], snake[0][1]-1])
    if current_dir == 0:
        snake.insert(0, [snake[0][0]-1, snake[0][1]])
    if current_dir == 2:
        snake.insert(0, [snake[0][0]+1, snake[0][1]])
    if not(0 < snake[0][0] <= N and 0 < snake[0][1] <= N) or snake.count(snake[0]) != 1: # 사과가 있느냐 없느냐 보다 장애물과 부딪혔는 지를 먼저 봄.
        live = False
    if apple_loc.count(snake[0]) == 0: # 사과가 없으면 꼬리를 자름
        snake.pop()
    else :
        apple_loc.remove(snake[0])
    end_time += 1
    if len(direction_info) > 0:
        if direction_info[0][0] == end_time:
            if direction_info[0][1] == 'L':
                current_dir = (current_dir-1) % 4
            else:
                current_dir = (current_dir+1) % 4
            direction_info.pop(0)
print(end_time)