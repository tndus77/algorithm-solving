n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
count = 0

def canGo(x, y, isDia):
  if x >= n or y >= n:
    return False
  elif lst[x][y] == 1:
    return False
  elif isDia and (lst[x-1][y] == 1 or lst[x][y-1] == 1):
    return False
  return True

def dfs(x, y, shape):
  global count
  if x == n-1 and y == n-1:
    count += 1
    return

  # 수평 -> 수평 or 대각선: 수직만 아니면, 수직 -> 수직 or 대각선: 수평만 아니면, 대각선 -> 수평 or 수직 or 대각선
  # 가로 0, 세로 1, 대각선 2
  nx = x+1
  ny = y+1
  if canGo(nx, ny, True):
    dfs(nx, ny, 2)
  
  # 수직만 아니면 -> 수평
  if shape != 1:
    nx = x
    ny = y + 1
    if canGo(nx, ny, False):
      dfs(nx, ny, 0)
  
  # 수평만 아니면 -> 수직
  if shape != 0:
    nx = x + 1
    ny = y
    if canGo(nx, ny, False):
      dfs(nx, ny, 1)

dfs(0, 1, 0)
print(count)