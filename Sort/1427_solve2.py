# 소트인사이드
# 수가 주어지면 그 수의 각 자리수를 내림차순으로 정렬해보자.

num = list(map(int, input()))
num.sort(reverse=True)

for i in num:
    print(i, end='')