"""
숫자 카드 게임
m : 가로
n : 세로
"""
"""
m,n = map(int, input().split())
cards = [list(map(int, input().split())) for _ in range(m)]

result = 0

for card in cards:
    smallest = min(card)
    if smallest > result :
        result = smallest

print(result)
"""

# 입력을 받으면서 바로 해결하기
n, m = map(int, input().split())

result = 0

for i in range(n):
    card = list(map(int, input().split()))
    result = max(min(card), result)  # NOTE 바로 변수에 큰 값 비교해서 넣기

print(result)
