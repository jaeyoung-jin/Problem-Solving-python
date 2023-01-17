# 커트라인

# n: 응시자 수, k: 입상자 수 -> k 번째 사람의 점수를 구하면 된다.
n, k = map(int, input().split())

scores = list(map(int, input().split()))
scores.sort(reverse=True)

print(scores[k-1])

