# 연구소 (문제 14052번)

def add_virus(map_virus, map_copy, virus_row, virus_col): # 함수로 바이러스가 전염될 수 있는 위치를 찾아서 바이러스 리스트에 추가하고 '0'을 '2'로 변경
    if 0<=virus_row-1<len(map_copy) and 0 <= virus_col<len(map_copy[0]) and map_copy[virus_row-1][virus_col] == 0:
        map_copy[virus_row-1][virus_col] = 2
        map_virus.append([virus_row-1, virus_col])
    if 0 <= virus_row <len(map_copy) and 0 <= virus_col-1 < len(map_copy[0]) and map_copy[virus_row][virus_col-1] == 0:
        map_copy[virus_row ][virus_col-1] = 2
        map_virus.append([virus_row, virus_col-1])
    if 0<=virus_row+1<len(map_copy) and 0 <= virus_col<len(map_copy[0]) and map_copy[virus_row+1][virus_col] == 0:
        map_copy[virus_row+1][virus_col] = 2
        map_virus.append([virus_row+1, virus_col])
    if 0<=virus_row<len(map_copy) and 0 <= virus_col+1<len(map_copy[0]) and map_copy[virus_row][virus_col+1] == 0:
        map_copy[virus_row][virus_col+1] = 2
        map_virus.append([virus_row, virus_col+1])
    return map_virus, map_copy

m, n = map(int, input().split()) # 지도 전체의 행열 크기를 입력 받고 m, n에 각각 행과 열의 길이를 저장

lab_map = [] # 지도를 나타내는 list 초기화
for i in range(0, m):  # 행길이 만큼 반복해서 2차원 list로 0, 1, 2 저장(0: 빈공간, 1: 벽, 2: 바이러스)
    lab_map.append([])
    lab_map[i] = list(map(int, input().split()))

map_empty = [] # 빈 공간의 위치를 리스트로 나타내기 위해 초기화
map_virus = [] # 바이러스 위치를 리스트로 초기화
for i in range(0, m): # 이중 반복문으로 빈 공간 위치 찾아서 저장
    for j in range(0, n):
        if lab_map[i][j] == 0: # 리스트의 값이 0인 곳이 빈 공간
            map_empty.append([i, j])
        elif lab_map[i][j] == 2: # 리스트의 값이 2인 곳이 바이러스 위치
            map_virus.append([i, j])
max_empty_area = 0
for i in range(0, len(map_empty)-2):
    for j in range(i+1, len(map_empty)-1):
        for k in range(j+1, len(map_empty)):
            map_copy = [] # 벽을 세우는 경우의 수마다 초기화
            for l in range(0, m): # 객체가 복사되지 않고 값이 복사되도록 1차원 리스트를 차례로 대입
                map_copy.append(lab_map[l].copy())  # 벽을 3개 세워야 하므로 최적 위치를 찾기 위해 지도를 복사
            empty_row, empty_col = map_empty[i] # 벽을 3개 세움
            map_copy[empty_row][empty_col] = 1
            empty_row, empty_col = map_empty[j]
            map_copy[empty_row][empty_col] = 1
            empty_row, empty_col = map_empty[k]
            map_copy[empty_row][empty_col] = 1
            map_virus_copy = map_virus.copy() # 기존의 바이러스 위치를 복사
            for virus_row, virus_col in map_virus_copy: # 새로 추가될 바이러스 위치를 추가
                map_virus_copy, map_copy = add_virus(map_virus_copy, map_copy, virus_row, virus_col) # 함수를 통해 추가될 바이러스 위치 찾은 후 추가
            empty_area = 0
            for map_row in range(m): # 안전 구역의 크기를 찾음
                empty_area += map_copy[map_row].count(0)
            if max_empty_area < empty_area: # 안전 구역의 크기가 기존 최댓값보다 크면 최대 안전 구역 크기를 변경
                max_empty_area = empty_area
print(max_empty_area) # 최대 안전 구역 크기 출력