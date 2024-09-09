"""
1. 5로 나누어 떨어지면, 5로 나눈다.
2. 3''
3. 2''
4. 1을 뺀다.

최소한의 연산 횟수
"""

x = int(input())

count = 0
result = x
while True:
    if result == 1:
        break

    if result % 5 == 0:
        result = result // 5
        count += 1
        continue

    elif result % 3 == 0:
        keep = result // 3
        if keep % 5 == 0:
            result = result // 3
            count += 1
            continue

    elif result % 2 == 0:
        keep = result // 2
        if keep % 5 == 0 :
            result = result // 2
            count += 1
            continue


    result -= 1
    count += 1


print(count)
