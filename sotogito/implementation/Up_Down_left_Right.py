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

array = [[0 for _ in range(n)] for _ in range(n)]

userX = 1
userY = 1

for direction in directionList:
    if direction == 'R' and userY + 1 <= n:
        userY += 1
    elif direction == 'L' and userY - 1 >= 1:
        userY -= 1
    elif direction == 'U' and userX - 1 >= 1:
        userX -= 1
    elif direction == 'D' and userX + 1 <= n:
        userX += 1


print(userX, userY)