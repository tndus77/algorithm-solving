import sys
sys.setrecursionlimit(10**6)

# 북, 북동, 동, 동남, 남, 남서, 서, 서북
dx = [-1, -1, 0, 1, 1, 1, 0, -1] # 행
dy = [0, 1, 1, 1, 0, -1, -1, -1] # 열

def dfs(graph, x, y):
  for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx < h and 0 <= ny < w and lst[nx][ny] == 1:
      # 이동
      lst[nx][ny] = 0
      dfs(graph, nx, ny)

while True:
  # 열, 행
  w, h = map(int, input().split())
  count = 0

  if w == 0 and h == 0: # 0 0을 만나면 나오기
    break

  lst = [list(map(int, input().split())) for _ in range(h)]

  for i in range(h):
    for j in range(w):
      if lst[i][j] == 1:
        dfs(lst, i, j)
        count += 1

  print(count)