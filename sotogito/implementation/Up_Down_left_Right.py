"""
문제:
5 : 가로, 새로 크기
RRRUDD :

1. 5*5 배열 생성
현재 사용자의 위치 1.1
R : [][+1]
L : [][-1]

U : [-1][]
D : [+1][]

밤위는 만약 가로 새로 가각 4가 넘어간다면 무시
"""

n = int(input())
directionList = input().split()

move_types = ['R', 'L', 'U', 'D']
xMove = [0, 0, -1, +1]
yMove = [+1, -1, 0, 0]

array = [[0 for _ in range(n)] for _ in range(n)]

userX = 1
userY = 1

for direction in directionList:
    for i in range(len(move_types)):
        if direction == move_types[i]:
            resultY = userY + yMove[i]
            resultX = userX + xMove[i]

    if resultY < 1 or resultY > n or resultX < 1 or resultX > n:
        continue

    userY = resultY
    userX = resultX

print(userX, userY)
