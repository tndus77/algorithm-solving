from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
dfs_visited = [False] * (n+1)
bfs_visited = [False] * (n+1)

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

dfsArr = []
bfsArr = []

def dfs(graph, v, visited):
  visited[v] = True
  dfsArr.append(v)

  s_graph = sorted(graph[v])
  for i in s_graph:
    if not visited[i]:
      dfs(graph, i, visited)

def bfs(graph, v, visited):
  visited[v] = True
  q = deque([v])

  while q:
    n = q.popleft()
    bfsArr.append(n)
    s_graph = sorted(graph[n])
    for i in s_graph:
      if not visited[i]:
        visited[i] = True
        q.append(i)
      
dfs(graph, v, dfs_visited)
print(' '.join(map(str, dfsArr)))
bfs(graph, v, bfs_visited)
print(' '.join(map(str, bfsArr)))