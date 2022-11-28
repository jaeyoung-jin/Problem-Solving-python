n = int(input())

# 최고점을 담을 변수
max = 0

# 점수를 담을 리스트
scores = list(map(int, input().split()))

# 점수 리스트를 하나씩 탐색하며 최고점을 담는다.
for i in range(n):
    if scores[i] > max:
        max = scores[i]

# 점수 리스트를 하나씩 탐색하며 점수를 바꿔 담는다.
for i in range(n):
    scores[i] = (scores[i]/max)*100

print(sum(scores)/len(scores))



