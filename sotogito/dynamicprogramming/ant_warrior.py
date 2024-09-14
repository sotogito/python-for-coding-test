"""
이 문제에서 dp리스트에 저장해둔 값의 의미가 뭘까


그니까 총 최대값을 구하는거는
1. 자신을 포함한 경우 i+(i-2)
2. 자신을 포함하지 않는 경우 i-1

겹치지 않는 선택 보장??
말 그대로 자신이 포함되면 i-1은 선택되지 않고, i-1이 선택되면 자신이 포함되지 않는다.
위의 로직 둘 중 하나를 비교하여 값을 매기기 떄문이다.


"""

n = int(input())
food = list(map(int, input().split()))
dp = [0] * n
result = 0

dp[0] = food[0]
dp[1] = max(food[0], food[1])


def calculate_max_food(n):
    for i in range(2, n):
        dp[i] = max(dp[i - 1], (dp[i - 2] + food[i]))
    return dp[n-1]


print(calculate_max_food(n))
