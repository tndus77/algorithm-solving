N = int(input())
M = N//2
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 100*M*M

def cal(alst, blst):
  asum = bsum = 0

  for i in range(M):
    for j in range(M):
      asum += arr[alst[i]][alst[j]]
      bsum += arr[blst[i]][blst[j]]

  return abs(asum - bsum)

def dfs(n, start, link):
  global ans

  if len(start) > M or len(link) > M:
    return
    
  if n == N:
    if len(start) == len(link) == M:
      ans = min(ans, cal(start, link))
    return

  # 스타트팀
  dfs(n+1, start+[n], link)
  # 링크팀
  dfs(n+1, start, link+[n])

dfs(0, [], [])
print(ans)