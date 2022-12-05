#개수세기
import sys 

#입력받을 정수의 개수
n = int(sys.stdin.readline())

#n개 요소 리스트
num_list = list(map(int,sys.stdin.readline().split()))

#찾고싶은 수
number = int(sys.stdin.readline())

#number의 개수를 체크할 변수
cnt = 0

#num_list 에서 number 개수 찾기
for i in num_list:
    if i==number:
        cnt+=1

print(cnt)
