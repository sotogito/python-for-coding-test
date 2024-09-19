"""
796,796으로 나눈 수 나머지..를 출력하는거였내ㅔ이럴수가

만약 짝수가 아닐경우 -1하면 dp[i-1]은 이미 구해졌잖아 거기에 1*2타일을 하나 더 넣으면 되니까

근데 내가 이해가 안되는건 1*2타일이 자리가 변경되었을대
즉, 맨 마지막이 아니라 맨 앞에 갔을때 그리고 이미 구한 dp[i-1]의 경우의 수에서
그 중간에 들어갈 경우 그 경우의 수는 어떻게 꼐산하냐 이말이야

dp[n−1]: 마지막에 1x2 타일을 세로로 하나 추가하는 경우.
dp[n−2]: 마지막에 1x2 타일을 가로로 두 개 추가하는 경우.
dp[n−2]: 마지막에 2x2 타일 하나를 추가하는 경우.

dp[n−2]에 1*2타일이 세로로 2개 놓여지는 경우의수는 dp[n−1]: 마지막에 1x2 타일을 세로로 하나 ㅊ가하는 겨웅에서 다루고있기 떄문에 고려하지 않는다.
"""

n = int(input())

dp = [0] * (n + 1)

dp[1] = 1
dp[2] = 3

for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2] * 2) % 796796
    # dp[i] += dp[i - 1]
    # dp[i] += dp[i - 2] * 2

print(dp[n])
