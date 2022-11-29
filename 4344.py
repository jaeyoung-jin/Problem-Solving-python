# 평균은 넘겠지

# 테스트케이스의 개수
n = int(input())

# 학생 수와 점수를 리스트로 입력받는다.
for _ in range(n):
    scores = list(map(int,input().split()))
    # 합계를 담을 변수
    sum_scores = 0

    # 모든 학생의 점수를 더한다.
    # sum(scores[1:])으로도 표현 가능
    # 위와같이 표현하면 평균도 한줄로 구할 수 있음
    for i in range(1, len(scores)):
        sum_scores += scores[i]
    mean_score = sum_scores/scores[0]

    # 평균보다 더 높은 점수를 담을 리스트
    # 리스트를 선언하지 않고, cnt 변수를 사용해서 수만 세고 넘어가도 됨
    upper = []
    for j in range(1,len(scores)):
        if scores[j]>mean_score:
            upper.append(scores[j])
    result = (len(upper)/scores[0])*100

    # 파이썬 소수점 출력 형식 지정 방법 따로 정리할 것
    print('{0:0.3f}%'.format(result))