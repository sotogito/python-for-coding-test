"""
숫자 카드 게임
m : 가로
n : 세로
"""

m,n = map(int, input().split())
cards = [list(map(int, input().split())) for _ in range(m)]

result = 0

for card in cards:
    smallest = min(card)
    if smallest > result :
        result = smallest

print(result)

