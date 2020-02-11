# 미세먼지 안녕! (문제 17144번)
def wind(house, cleaner, R, C): # 공기청정기 바람
    for r in range(cleaner-2, 0, -1):
        house[r][0] = house[r-1][0]
    for r in range(cleaner+1, R-1):
        house[r][0] = house[r+1][0]
    for c in range(C-1):
        house[0][c] = house[0][c+1]
        house[R-1][c] = house[R-1][c+1]
    for r in range(0, cleaner-1):
        house[r][C-1] = house[r+1][C-1]
    for r in range(R-1, cleaner, -1):
        house[r][C-1] = house[r-1][C-1]
    for c in range(C-1, 1, -1):
        house[cleaner-1][c] = house[cleaner-1][c-1]
        house[cleaner][c] = house[cleaner][c-1]
    house[cleaner-1][1] = 0
    house[cleaner][1] = 0
    return house

R, C, T = map(int, input().split()) # 행, 열, 시간을 입력 받음

house = [] # 집안의 좌표별 미세먼지 양과 공기청정기의 위치
moved_dust =[] # 움직인 미세먼지 양의 위치
total_dust = 0 # 남아 있는 먼지 총량
for r in range(R):
    house.append([])
    house[r] = list(map(int, input().split()))
    moved_dust.append([0]*C)
    if house[r][0] == -1:
        cleaner = r
for t in range(T):
    for r in range(R):
        for c in range(C):
            if house[r][c] != -1 and house[r][c] != 0: # 해당 좌표에서 미세먼지 확산
                spread = 0 # 확산하는 방향의 수
                amount = int(house[r][c]/5)
                if 0 <= r-1 < R and 0 <= c < C and house[r-1][c] != -1:
                    spread += 1 #확산 방향 추가
                    moved_dust[r-1][c] += amount
                if 0 <= r < R and 0 <= c-1 < C and house[r][c-1] != -1:
                    spread += 1
                    moved_dust[r][c-1] += amount
                if 0 <= r+1 < R and 0 <= c < C and house[r+1][c] != -1:
                    spread += 1 #확산 방향 추가
                    moved_dust[r+1][c] += amount
                if 0 <= r < R and 0 <= c+1 < C and house[r][c+1] != -1:
                    spread += 1
                    moved_dust[r][c+1] += amount
                house[r][c] -= amount * spread
    for r in range(R): # 미세먼지 확산 후의 좌표마다 바뀐 양을 표현
        for c in range(C):
            house[r][c] += moved_dust[r][c]
        moved_dust[r] = [0]*C
    house = wind(house, cleaner, R, C)
for r in range(R):
    total_dust += sum(house[r])
print(total_dust+2)