# 그룹 단어 체커
n = int(input())


# 그룹단어 개수를 체크할 변수 cnt 선언
cnt = 0

# n번 반복
for _ in range(n):
    # 이전에 나왔던 문자들을 담아두는 리스트 previous_ch 선언
    previous_ch = []

    flag = 0
    input_string = input()

    # 문자열은 리스트로 자동 취급 가능 -> 하나씩 체크해야 한다.
    # 체크해야할 것
    # 이전에 나온 적 있는 문자인가?
    # 1. 이전에 나온 적 있는 문자라면
    # 1-1. 바로 이전 문자와 같지 않다면 -> 그룹단어가 아니므로 체크를 중단한다.(break)
    # 1-2. 바로 이전 문자와 같다면 -> 계속 체크를 진행한다.(continue)


    # 2. 이전에 나온 적 없는 문자라면
    # 2-1. 이전에 나온 문자들을 담는 배열에 저장한다.
    
    for i in range(len(input_string)):
        # 기존에 나왔던 문자의 경우
        if input_string[i] in previous_ch:
            # 첫 번째 문자가 해당 블록에 들어올 가능성은 없다.(index error 가능성 없음)
            # 바로 이전 문자와 같은지 비교해준다.
            # 바로 이전 문자와 같은 경우
            if input_string[i] == input_string[i-1]:
                continue

            # 바로 이전 문자와 같지 않은 경우
            else:
                # 체크를 중단하고 반복문을 빠져나간다. 
                flag = 1
                break

        # 기존에 나오지 않았던 문자의 경우
        else:
            # previous_ch에 추가해준다.
            previous_ch.append(input_string[i])

    if flag == 0:
        cnt +=1

print(cnt)
            



