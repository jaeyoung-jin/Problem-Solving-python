# 셀프 넘버

# 생성자 n을 통해 생성자가 있는 수(셀프넘버가 아닌 수)를 구하는 함수를 정의한다.
def d(n: int) -> int:
    n = n + sum(map(int,str(n)))
    return n

# 생성자가 있는 수(셀프 넘버가 아닌 수)를 넣을 집합
non_selfnum = set()

# 1부터 10000까지의 수를 이용해 생성자가 있는 수(셀프 넘버가 아닌 수)를 구한다.
for i in range(1, 10001):
    non_selfnum.add(d(i))

# 셀프 넘버를 출력한다.
for i in range(1, 10001):
    if i not in non_selfnum:
        print(i)
