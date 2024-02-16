n = int(input())
lst = list(map(int, input().split()))
dp = [sum] * len(lst)
dp[0] = lst[0]

for i in range(1, n):
   dp[i] = max(dp[i-1] + lst[i], lst[i]) # dp[i-1]+본인 값과 본인 값 비교

print(max(dp))