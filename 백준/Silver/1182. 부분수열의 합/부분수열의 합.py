n, s = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

def dfs(idx, sum):
  global ans
  if idx >= n:
    return
  sum += arr[idx]

  if sum == s:
    ans += 1
  
  dfs(idx+1, sum) # 현재 arr[idx]를 선택하는 경우의 가지

  dfs(idx+1, sum - arr[idx]) # 현재 arr[idx]를 선택하지 않는 경우의 가지

dfs(0, 0)
print(ans)