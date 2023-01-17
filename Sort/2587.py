# 대표값2

nums = []

for _ in range(5):
    nums.append(int(input()))

nums.sort()
num_mean = sum(nums)/len(nums)

print(int(num_mean))
print(nums[2])