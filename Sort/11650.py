# 좌표 정렬하기
import sys
input = sys.stdin.readline

n = int(input())

location = []

for _ in range(n):
    location.append(list(map(int, input().split())))

location.sort()

for i in range(n):
    print(location[i][0], location[i][1])
    


