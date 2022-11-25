#더하기 사이클 
first, second = 0

#사이클 길이 측정을 위한 변수
cnt = 0

#숫자 입력 받기
num = int(input())

while(True):

    first = num//10
    second = num%10

    new_num = first + second

    if num == first*10 + second*1: break 