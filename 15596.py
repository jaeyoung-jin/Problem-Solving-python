# 정수 N개의 합

# a 에는 list가 들어가야 하고, 리턴 값은 int 타입이어야 한다.(파이썬 타입 힌트)
def solve(a: list) -> int:
    sum = 0
    for num in a:
        sum+=num

# return sum(a) 로 하면 시간과 코드 길이가 절반 이상으로 줄어든다.
    return sum




