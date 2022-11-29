# OX퀴즈

n = int(input())

for _ in range(n):
    score = 0
    result = 0
    #문자열을 입력받아 리스트로 사용
    # answers = input()
    # answers = list(map(str,input())) 
    answers = list(input())

    for answer in answers:
        if answer == 'O':
            score+=1

        elif answer == 'X':
            score=0

        result += score
    
    print(result)

