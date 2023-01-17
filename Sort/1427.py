# 소트인사이드
# 수가 주어지면 그 수의 각 자리수를 내림차순으로 정렬해보자.

num = input()
num_list = []

for i in range(len(num)):
    num_list.append(num[i])

num_list.sort(reverse=True)

print(''.join(map(str, num_list)))

