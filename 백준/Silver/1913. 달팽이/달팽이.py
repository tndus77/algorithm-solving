import sys

N = int(input())
findNum = int(input())

board = [[0] * N for _ in range(N)]
x = (N-1)//2
y = (N-1)//2
board[x][y] = 1

# 상, 우, 하, 좌
dx = [-1, 0, 1, 0] # 행
dy = [0, 1, 0, -1] # 열

i = 2 # 2부터 시작
start = 3 # N=3부터 시작

while x != 0 and y != 0:
  while i <= start * start:
    if x == y == (N-1)//2: #시작점이면
      top, right, bottom, left = start, start-2, start-1, start-1
      # 위로 한칸
      x += dx[0]
      y += dy[0]
      top -= 1
    elif right > 0:
      x += dx[1]
      y += dy[1]
      right -= 1
    elif bottom > 0:
      x += dx[2]
      y += dy[2]
      bottom -= 1
    elif left > 0:
      x += dx[3]
      y += dy[3]
      left -= 1
    elif top > 0:
      x += dx[0]
      y += dy[0]
      top -= 1
    board[x][y] = i
    i += 1
  N -= 2
  start += 2

findX, findY = 0, 0
for i in range(len(board)):
  print(*board[i])
  if findNum in board[i]:
    findX = i + 1
    findY = board[i].index(findNum) + 1

print(findX, findY)
