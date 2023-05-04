# 수학은 비대면강의입니다.

import sys
input = sys.stdin.readline

a, b, c, d, e, f = map(int, input().split())

# x와 y가 각각 -999 이상 999이하의 정수인 경우만 입력으로 주어짐이 보장된다.

for x in range( -999, 1000):
    for y in range(-999, 1000):

        if (a * x) + (b * y) == c and (d * x) + (e * y) == f:
            print(x, y)
            