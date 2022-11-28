# X보다 작은 수
# 정수의 개수 n, 기준 정수 x
n, x = map(int, input().split())

# 리스트 a
a = list(map(int, input().split()))

# 기준 정수 x보다 작은 값들을 넣을 리스트
small_nums = []

for num in a:
    if num < x:
        small_nums.append(num)

for small_num in small_nums:
    print(small_num,end=' ')
    

