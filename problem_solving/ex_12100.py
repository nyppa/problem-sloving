# 2048(easy) (12100번 문제)
from collections import deque
N = int(input())
board = []
for i in range(N):
    board.append(list(map(int, input().split())))
try_num = 0
def game2048(try_num, board):
    len_board = len(board)
    if try_num == 5:
        max_num = 0
        for i in range(len_board):
            if max_num < max(board[i]):
                max_num = max(board[i])
        return max_num
    max_list = [0]*4
    board_copy = [] # 보드를 4개 복사해서 4방향에서 결과 출력
    for i in range(4):
        board_copy.append([])
        for j in range(len_board):
            board_copy[i].append([])
            if i == 0: # 오른쪽으로 미는 보드
                board_copy[i][j] = board[j].copy()
            elif i == 1: # 왼쪽으로 미는 보드
                board_copy[i][j] = list(reversed(board[j].copy()))
            elif i == 2: # 위쪽으로 미는 보드
                for k in range(len_board):
                    board_copy[i][j].append(board[k][j])
            else:
                board_copy[i][j] = list(reversed(board_copy[2][j].copy()))
    # 오른쪽으로 밀기
    for k in range(4):
        for i in range(len_board):
            pass_index = -1  # 이미 합쳐져서 지나치는 인덱스
            move_list = []
            for j in range(len_board): # 0이 아닌 것만 복사
                if board_copy[k][i][j] != 0:
                    move_list.append(board_copy[k][i][j])
            for j in range(len(move_list)-1, -1, -1):
                if j == pass_index or j == 0:
                    continue # 다음 인덱스로 넘어감 (이미 더해진 인덱스이거나 길이가 1일때)
                else: # 넘어가지 않을 경우
                    if move_list[j] == move_list[j-1]:
                        pass_index = j-1
                        move_list.pop(j)
                        move_list[j-1] *= 2
            board_copy[k][i] = [0] * (len_board-len(move_list))
            board_copy[k][i].extend(move_list.copy())
        max_list[k] = game2048(try_num+1, board_copy[k])
    return max(max_list)
max_num = game2048(try_num, board)
print(max_num)