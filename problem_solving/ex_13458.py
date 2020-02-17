# 시험 감독 (13458번 문제)
import math
room_num = int(input())
student = list(map(int, input().split()))
B, C = map(int, input().split())
supervisor = []
for i in range(room_num):
    supervisor.append(math.ceil(max(0, ((student[i]-B)/C))))
print(sum(supervisor) + room_num)