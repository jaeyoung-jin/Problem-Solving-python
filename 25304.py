#백준 25304번 영수증 문제

#입력한 총 금액과 비교해볼 계산 결과 금액 변수
result_price = 0

#총 금액 입력
total_price = int(input())

#구매한 물건의 종류수
n = int(input())

#물건의 가격과 개수가 나열된다.
for _ in range(n):
    price, num = map(int, input().split())
    result_price += price*num

if result_price == total_price: print("Yes")
else: print("No")
