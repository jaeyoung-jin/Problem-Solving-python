# 색종이

# 도화지 만들기
field = [[0 for _ in range(100)] for _ in range(100)]

n = int(input())

for _ in range(n):
    # 첫 번째 자연수는 색종이의 왼쪽 변과 도화지의 왼쪽 변 사이의 거리(n -> index n열 부터 10칸 만큼 색종이를 붙인다.)
    # 두 번째 자연수는 색종이의 아래쪽 변과 도화지의 아래쪽 변 사이의 거리(m -> index 99-m행 부터 10칸 만큼 색종이를 붙인다.)
    n, m = map(int, input().split())

    # 첫 번째 자연수는 왼쪽 변과의 거리이므로 점차 증가해가면서 칠해주어야 한다.
    # 두 번째 자연수는 아래쪽 변과의 거리이므로 점차 감소해가면서 칠해주어야 한다.
    for i in range(10):
        for j in range(10):
    
            # 해당 위치의 값을 1로 바꾸어준다.
            field[99-m-j][n+i] = 1

# 1의 개수를 센다.
result = 0

for row in range(100):
    for col in range(100):
        if field[row][col] == 1:
            result += 1

print(result)
        

    
