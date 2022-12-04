# 문자열 반복

# 테스트 케이스 개수
t = int(input())

# 각 테스트 케이스
for _ in range(t):

    # 반복 횟수와 문자열 모두 str로 입력 받는다.
    r, s = map(str, input().split())
    for i in s:
        print(i*int(r),end='')

    print()