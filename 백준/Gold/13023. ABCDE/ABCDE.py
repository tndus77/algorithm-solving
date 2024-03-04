# 사람의 수, 친구 관계의 수
N, M = map(int, input().split())
graph = [[] for _ in range(N)]
visited = [False] * N

for _ in range(M):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

ans = 0
def dfs(graph, n, v, visited):
  global ans
  visited[v] = True
  if n == 4:
    ans = 1
    return
  for i in graph[v]:
    if not visited[i]:
      visited[i] = True
      dfs(graph, n+1, i, visited)
      visited[i] = False

for i in range(N):
  # 친구 관계 탐색
  dfs(graph, 0, i, visited)
  visited[i] = False # 방문 표시 해제
  if ans == 1:
    break

print(ans)