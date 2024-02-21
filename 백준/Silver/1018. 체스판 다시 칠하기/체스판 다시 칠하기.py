# 행, 열
n, m = map(int, input().split())
board = [] # 체스판 정보 리스트
repair = [] # 다시 칠해야할 개수 저장할 리스트
for _ in range(n):
  board.append(input())

for i in range(n-7):
  for j in range(m-7):
    white = 0
    black = 0
    for k in range(i, i+8):
      for l in range(j, j+8):
        if (k+l) % 2 == 0: # 흰색 or 검은색
          if board[k][l] != 'W':
            white += 1
          if board[k][l] != 'B':
            black += 1
        else:
          if board[k][l] != 'W':
            black += 1
          if board[k][l] != 'B':
            white += 1
    repair.append(white)
    repair.append(black)

print(min(repair))