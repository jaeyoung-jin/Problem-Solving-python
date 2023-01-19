# 좌표 정렬하기(튜플로 받기)
import sys
input = sys.stdin.readline

n = int(input())

location = []
for _ in range(n):
    location.append(tuple(map(int, input().split())))
    
location.sort(key=lambda x: (x[0], x[1]))

for i in location:
    print(i[0], i[1])




