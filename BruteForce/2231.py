# 분해 합
import sys
input = sys.stdin.readline


# 자연수 n이 있을 때, 그 자연수 n의 분해합은 n과 n을 이루는 각 자리수의 합을 의미한다.
# 어떤 자연수 m의 분해합이 n인 경우, m을 n의 생성자라고 한다.

# ex) 245의 분해합 256 --> 245가 생성자

n = int(input())
flag = 0


# 분해합이 n인 수를 모두 찾는다.
for i in range(1, n):
    result = i
    for num in str(i):
        result += int(num)

    if result == n:
        flag = 1
        print(i)
        break

if flag == 0:
    print(0)

