from collections import deque

# 물품의 수, 최대 무게
N, K = map(int, input().split())
bag = deque()
dp = [0] * (K+1)

# 물건의 무게, 가치
for _ in range(N):
  w, v = map(int, input().split())
  bag.append((w, v))

for _ in range(N):
  weight, value = bag.popleft()
  for i in range(K, weight-1, -1):
    dp[i] = max(dp[i], dp[i-weight]+value) # 현재 값, 현재 값 제외

print(dp[K])