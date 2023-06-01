# 영화감독 숌
# 모든 숫자 중에서, 666이 포함된 숫자들의 순서를 매기는 것

import sys
input = sys.stdin.readline

n = int(input())

# 666이 포함된 숫자 중 가장 작은 숫자를 초기 세팅(반복문의 반복 횟수를 최대한 줄이기 위함)
value = 666

# 몇 번째로 작은 수인지 세기 위한 변수
cnt = 0

# 정확한 반복 횟수를 미리 측정할 수 없는 경우이므로 while
while True:

    # 만약 value에 666이 포함되어 있다면
    if '666' in str(value):
        # cnt를 증가시켜 value에 순서를 매겨주고
        cnt += 1
        # 매겨준 순서가 사용자가 입력한 값과 일치한다면
    if cnt == n:
        # 현재 value를 출력해준 후 break
        print(value)
        break
    # 아직 사용자가 입력한 값과 일치하지 않는 상태라면, value를 하나 증가시킨 후 다시 비교 
    value += 1



