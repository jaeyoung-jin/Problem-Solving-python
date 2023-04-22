# 블랙잭
import sys
input = sys.stdin.readline

# 카드의 개수 n
n, m = map(int, input().split())

# 카드에 쓰여있는 n개의 수들
nums = sorted(list(map(int, input().split())))

result_list = []

# m을 넘지 않으면서 m에 최대한 가까운 카드 3장의 합을 출력한다.

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        for k in range(j+1, len(nums)):
            sumOfNums = nums[i] + nums[j] + nums[k]
            
            if sumOfNums > m:
                break
            else:
                result_list.append(sumOfNums)

print(max(result_list))

            
            



