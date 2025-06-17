import sys

n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]

coins = list(filter(lambda x: x <= k, coins))

cnt = 0
for i in range(len(coins)-1, -1, -1):
  curr = coins[i]
  if k <= 0:
    break
  if k < curr:
    continue
  
  cnt += k // curr
  k %= curr

print(cnt)