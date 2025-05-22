N, M = map(int, input().split())
r, c, d = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
cnt = 0 # 청소하는 칸의 개수
# 북, 동, 남, 서
dr = [-1, 0, 1, 0] #행
dc = [0, 1, 0, -1] #열

while True:
  # 조건 1
  if board[r][c] == 0:
    board[r][c] = 2 # 청소 완
    cnt += 1
  
  # 4칸 모두 청소 되었는지 체크 (모두 청소되어있으면 False 유지, 청소되지 않은 칸이 있으면 True)
  flag = False
  for _ in range(4):
    # 왼쪽으로 회전
    d = (d + 3) % 4
    nx = r + dr[d]
    ny = c + dc[d]

    # 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
    if board[nx][ny] == 0:
      r, c = nx, ny
      flag = True
      break
  
  # 모두 청소되어 있다면
  if not flag:
    # 후진
    back = (d + 2) % 4
    nx = r + dr[back]
    ny = c + dc[back]

    if board[nx][ny] == 1:
      break
    else:
      r, c = nx, ny
  
print(cnt)