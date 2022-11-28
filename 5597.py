# 과제 안 내신 분..?

# 과제 제출자 출석번호 입력 받기
submit = []
for _ in range(28):
    n = int(input())
    submit.append(n)

# 과제 제출자 출석번호 순서대로 정렬
submit.sort()

for i in range(1, 31):
    if i not in submit:
        print(i)


