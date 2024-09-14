"""
이 문제에서 dp리스트에 저장해둔 값의 의미가 뭘까


그니까 총 최대값을 구하는거는
1. 자신을 포함한 경우 i+(i-2)
2. 자신을 포함하지 않는 경우 i-1

겹치지 않는 선택 보장??
말 그대로 자신이 포함되면 i-1은 선택되지 않고, i-1이 선택되면 자신이 포함되지 않는다.
위의 로직 둘 중 하나를 비교하여 값을 매기기 떄문이다.

그리고 max를 비교할때 food[]로 비교하는데 아니라 전에 계산하여 최대값을 저장해 두었던 dp[]에서 꺼내 비교 한다는 걸 잊지 말자

아래는 동작하는 예시이다.
[1, 15, 11, 12, 40, 25, 50, 30, 20, 60]

dp[0] = food[0] = 1
dp[1] = max(food[0], food[1]) = max(1, 15) = 15

dp[2] = max(dp[1], dp[0] + food[2]) = max(15, 1 + 11) = 15
dp[3] = max(dp[2], dp[1] + food[3]) = max(15, 15 + 12) = 27
dp[4] = max(dp[3], dp[2] + food[4]) = max(27, 15 + 40) = 55
dp[5] = max(dp[4], dp[3] + food[5]) = max(55, 27 + 25) = 55
dp[6] = max(dp[5], dp[4] + food[6]) = max(55, 55 + 50) = 105
dp[7] = max(dp[6], dp[5] + food[7]) = max(105, 55 + 30) = 105
dp[8] = max(dp[7], dp[6] + food[8]) = max(105, 105 + 20) = 125
dp[9] = max(dp[8], dp[7] + food[9]) = max(125, 105 + 60) = 165
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
