import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ans = []
def dfs(n, lst):
  if n == M:
    ans.append(lst)
    return
  
  for i in range(1, N+1):
    dfs(n+1, lst+[i])
v = [0] * (N+1)
dfs(0, [])

for an in ans:
  print(*an)