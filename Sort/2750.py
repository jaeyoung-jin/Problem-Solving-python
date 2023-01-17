# 수 정렬하기
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

n = int(input())

num = []

for _ in range(n):
    num.append(int(input()))

num.sort()

for i in num:
    print(i)
