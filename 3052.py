# 나머지
remainder = []

for _ in range(10):
    n = int(input())
    remainder.append(n%42)

# 나머지 값 리스트를 하나씩 탐색하며 이미 있다면 결과 리스트에 담지 않는다.
results = []
for num in remainder:
    if num in results:
        continue
    else: 
        results.append(num)

print(len(results))
