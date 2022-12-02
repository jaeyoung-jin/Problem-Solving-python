# 알파벳 찾기

s = input()
alphabets = "abcdefghijklmnopqrstuvwxyz"

for alphabet in alphabets:
    if alphabet in s:
        print(s.index(alphabet), end=' ')

    else:
        print(-1, end=' ')