import sys
sys.setrecursionlimit(100000) #없으면 recursion error 발생
m, n, k = map(int, input().split()) #m=x, n=y
graph = [[0]*n for _ in range(m)]

# 북, 동, 남, 서
dx = [-1, 0, 1, 0] #행
dy = [0, 1, 0, -1] #열
count = 0
area = 0
result = []

def dfs(x, y):
  global area
  graph[x][y] = 1

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx > -1 and ny > -1 and nx < m and ny < n and graph[nx][ny] == 0:
      # 인접 노드로 이동
      area += 1
      dfs(nx, ny)


for _ in range(k):
  x1, y1, x2, y2 = map(int, input().split())
  for i in range(y1, y2):
    for j in range(x1, x2):
      graph[i][j] = 1 # 해당 부분은 이미 방문 처리로 ~

for i in range(m):
  for j in range(n):
    if graph[i][j] == 0: # 방문 안된 것만
      area = 1
      dfs(i, j)
      result.append(area)
      count += 1

result.sort()
print(count)
print(' '.join(map(str, result)))
  