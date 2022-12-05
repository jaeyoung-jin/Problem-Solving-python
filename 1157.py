# 단어 공부

# 문자열.upper(): 해당 문자열을 대문자로
# 문자열.lower(): 해당 문자열을 소문자로 
# 문자열.isupper(): 해당 문자열이 대문자인지 판단
# 문자열.count(s): 해당 문자열에서 s의 개수를 반환

word = input()
word = word.upper()

# 중복 없는 문자열 
word_set = list(set(word))

# 각 알파벳의 개수를 담을 리스트 선언
cnt = []
for s in word_set:
    cnt.append(word.count(s))

if cnt.count(max(cnt)) > 1:
    print("?")

else:
    print(word_set[cnt.index(max(cnt))])


