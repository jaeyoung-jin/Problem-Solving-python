# 좌표 압축
# 리스트 내부의 자신보다 작은 수의 개수를 센다.
# 같은 값의 작은 수가 2개라면 1개로 센다.

import sys
input = sys.stdin.readline


n = int(input())

nums = list(map(int, input().split()))
nums_set = sorted(list(set(nums)))

result = {nums_set[i]: i for i in range(len(nums_set))}


print(*[result[num] for num in nums], sep=' ')

