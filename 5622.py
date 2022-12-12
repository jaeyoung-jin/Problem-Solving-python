# 다이얼
s = input()


alphabets = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

cnt = 0 

for i in range(len(s)):
    for j in range(2, 10):
        if s[i] in alphabets[j-2]:
            cnt += (j-1)+2

print(cnt)
