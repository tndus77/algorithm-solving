n = int(input())
board = [list(map(int, input())) for _ in range(n)]
answer = []

def quad_tree(x, y, N):
  point = board[x][y]

  for i in range(x, x+N):
    for j in range(y, y+N):
      if point != board[i][j]:  # 같지 않은 색이 있다면
        answer.append('(')
        half = N // 2
        quad_tree(x, y, half)  # 2사분면 (왼쪽 위)
        quad_tree(x, y + half, half)  # 3사분면 (오른쪽 위)
        quad_tree(x + half, y, half)  # 1사분면 (왼쪽 아래)
        quad_tree(x + half, y + half, half)  # 4사분면 (오른쪽 아래)
        answer.append(')')
        return

  if point == 1:
      answer.append('1')
  else:
      answer.append('0')
quad_tree(0, 0, n)
print(''.join(answer))