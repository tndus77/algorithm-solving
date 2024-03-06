import sys
sys.setrecursionlimit(10**6)
n = int(input())
area = [list(input()) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

three_cnt = 0 # 적록색약이 아닌 사람
two_cnt = 0 # 적록색약인 사람
# 1. 적록색맹이 아닐 때 영역의 개수
# 2. R -> G로 모두 변경
# 3. 적록색맹일 때 영역의 개수

#북, 동, 남, 서
dx = [-1, 0, 1, 0] #행
dy = [0, 1, 0, -1] #열

def dfs(alph, x, y):
  visited[x][y] = True

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and area[nx][ny] == alph:
      dfs(area[nx][ny], nx, ny)

# 1.
for i in range(n):
  for j in range(n):
    if not visited[i][j]:
      dfs(area[i][j], i, j)
      three_cnt += 1

# 2.
for i in range(n):
  for j in range(n):
    if area[i][j] == 'R':
      area[i][j] = 'G'

visited = [[False]*n for _ in range(n)] # 초기화
# 3.
for i in range(n):
  for j in range(n):
    if not visited[i][j]:
      dfs(area[i][j], i, j)
      two_cnt += 1
print(three_cnt, two_cnt)