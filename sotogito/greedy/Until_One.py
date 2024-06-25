"""
1이 될떄까지
n : 1이 돼야하는 수
k : n에서 나누는 수

1. n에서 1을 뺀다
2. n에서 k로 나누다.
"""

"""
def until_one(n, k):
    if n % k == 0:
        return n // k
    return n - 1


n, k = map(int, input().split())

count = 0

while True:
    n = until_one(n, k)
    count += 1
    if n == 1:
        print(count)
        break
"""

n, k = map(int, input().split())

result = 0

# TODO 마저 풀어야됨ㅁ
