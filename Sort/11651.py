# 좌표 정렬하기 2
import sys
input = sys.stdin.readline

n = int(input())

location = []
for _ in range(n):
    location.append(tuple(map(int, input().split())))
    
location.sort(key=lambda x: (x[1], x[0]))

for i in location:
    print(i[0], i[1])




