"""
큰 수의 법칙
m : 인덱스 총 길이
k : 인덱스 최대 연속
"""
"""
n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort(reverse=True)

result = []
while len(result) != m:
    for _ in range(k):
        result.append(numbers[0])
    result.append(numbers[1])

print(sum(result))
"""

n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort(reverse=True)

result = 0

count = m // (k + 1) # 0000 0000
additionalCount = m - (count * (k + 1)) # 0000 0000 0

result += count * (k * numbers[0])
result += count * numbers[1]
result += additionalCount * numbers[0]

print(result)
