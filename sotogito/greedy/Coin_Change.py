"""
거스름돈
"""

amount = 1260
count = 0

coins = [500, 100, 50, 10]

for coin in coins:
    count += amount // coin
    amount %= coin

print(count)