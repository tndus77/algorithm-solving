# 북, 동, 남, 서
dx = [-1, 0, 1, 0] # 행
dy = [0, 1, 0, -1] # 열

N = int(input())
findNum = int(input())
num = 1

arr = [[0] * N for _ in range(N)]

x = N// 2
y = N// 2
arr[x][y] = 1

i = 2
start = 3

while x != 0 or y != 0:
  while i <= start * start:
    if x == y == N// 2: # 시작값이면
      up, right, down, left = start, start-2, start-1, start-1
      x += dx[0]
      y += dy[0]
      up -= 1

    elif right > 0:
      x += dx[1]
      y += dy[1]
      right -= 1
    
    elif down > 0:
      x += dx[2]
      y += dy[2]
      down -= 1
    
    elif left > 0:
      x += dx[3]
      y += dy[3]
      left -= 1

    elif up > 0:
      x += dx[0]
      y += dy[0]
      up -= 1
    arr[x][y] = i
    i += 1
  N -= 2
  start += 2

for i in range(len(arr)):
  print(*arr[i])
  for j in range(len(arr)):
    if arr[i][j] == findNum:
      x, y = i, j
print(x+1, y+1)