#더하기 사이클 

#첫째 자리 수와 둘째 자리 수
first, second = 0, 0

#사이클 길이 측정을 위한 변수
cnt = 0

#숫자 입력 받기
num = int(input())

#첫째 자리 수와 둘째 자리 수 구하기
first = num//10
second = num%10

while(True):
    cnt+=1
    new_num = first + second

    if new_num >= 10:
        first = second
        second = new_num%10
    else:
        first = second
        second = new_num

    if num == first*10 + second*1: break 

print(cnt)