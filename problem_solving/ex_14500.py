# 테트로미노 (14500번 문제)
N, M = map(int, input().split())
grid = [[]]*8
grid[0] = [list(map(int, input().split())) for i in range(N)] # 기본 그리드
grid[1] = grid[0][::-1] # 뒤집은 그리드
grid[2] = list(zip(*(grid[0]))) # transpose
grid[3] = list(zip(*(grid[1]))) # 뒤집고 transpose
grid[4] = grid[2][::-1] # transpose 뒤집기
grid[5] = list(zip(*(grid[4]))) # transpose 뒤집고 trasnpose
grid[6] = grid[5][::-1] # trasnpose 뒤집고 transpose 뒤집기
grid[7] = grid[3][::-1] # 뒤집고 transpose 뒤집기
max_tet = 0
def tet_sum(grid, N, M):
    tet = 0
    for i in range(N):
        for j in range(M-3):
            tet = max(tet, grid[i][j]+grid[i][j+1]+grid[i][j+2]+grid[i][j+3])
    for i in range(N-1):
        for j in range(M-1):
            tet = max(tet, grid[i][j]+grid[i][j+1]+grid[i+1][j]+grid[i+1][j+1])
    for i in range(N-1):
        for j in range(M-2):
            tet = max(tet, grid[i][j]+grid[i][j+1]+grid[i][j+2]+grid[i+1][j])
            tet = max(tet, grid[i][j+1]+grid[i][j+2]+grid[i+1][j]+grid[i+1][j+1])
            tet = max(tet, grid[i][j]+grid[i][j+1]+grid[i][j+2]+grid[i+1][j+1])
    return tet

for i in range(8):
    max_tet = max(max_tet, tet_sum(grid[i], len(grid[i]), len(grid[i][0])))
print(max_tet)