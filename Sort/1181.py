# 단어 정렬
# 반복문으로 여러 줄 입력 받아야 하는 경우에 input()을 사용한다면 시간이 굉장히 오래 걸린다.
# sys.stdin.readline은 개행 문자를 포함한다.
import sys

input = sys.stdin.readline

n = int(input())

# sys.stdin.readline()은 '한 줄' 단위로 입력을 받기 때문에 개행 문자를 제거해 주어야 한다.
words = [input().strip() for _ in range(n)]

# 중복 문자를 제거하기 위해 set으로 형 변환 했다가 다시 list로 형 변환
words = list(set(words))

# 1순위는 길이, 2순위는 사전 순 이라면 어떻게 코드를 작성해야 할까?
# words.sort()
# words.sort(key= len)

words.sort(key= lambda x: (len(x), x))

for word in words:
    print(word)




