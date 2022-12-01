# 한수: 각 자리가 등차수열을 이루는 수
# 숫자에 str() 함수를 적용하면 리스트처럼 사용 가능하다.(각 자릿수를 분리)

n = int(input())

def hansu(n: int) -> int:
    cnt = 0
    for i in range(1, n+1):
        # 100 미만은 모두 한수
        if i < 100:
            cnt+=1
        else:
            # i를 문자열로 바꾸고(리스트화) 각 자릿수에 int 함수 적용하여 리스트를 만든다.
            nums = list(map(int, str(i)))
            if nums[1]-nums[0] == nums[2]-nums[1]:
                cnt+=1
    return cnt

print(hansu(n))
