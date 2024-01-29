import sys
n = int(input())
m = int(input()) # 간선수 
node = [[] for i in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
  a, b = map(int, sys.stdin.readline().split())
  node[a] += [b]
  node[b] += [a]

def dfs(v):
  visited[v] = 1

  for nx in node[v]:
    if visited[nx] == 0:
      dfs(nx)

dfs(1)
print(sum(visited) - 1)