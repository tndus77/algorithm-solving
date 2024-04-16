import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ans = []

# s는 고른 숫자
def dfs(n, s, lst):
  if n == M:
    ans.append(lst)
    return
  
  for i in range(1, N+1):
    if i < s:
      continue
    dfs(n+1, i, lst+[i])

dfs(0, 1, [])
for an in ans:
  print(*an)