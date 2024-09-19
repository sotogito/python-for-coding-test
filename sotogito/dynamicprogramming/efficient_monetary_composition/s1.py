"""
N : 화폐의 종류
M : 총 합

최종이 7이고, 동저니 2,3,5까지 있다고 가정하면.
"""
n, m = map(int, input().split())
coin = []
for i in range(n):
    coin.append(i)

dp = [10001] * (m + 1)

dp[0] = 0

for i in range(n):
    for j in range(coin[i], m + 1):
        if dp[j - coin[i]] != 10001:
            dp[j] = min(dp[j], dp[j - coin[i]] + 1)  # 해당 동전만 포함 or 해당동전+나머지 동전

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])
