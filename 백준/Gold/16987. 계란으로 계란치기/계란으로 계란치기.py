import sys
input = sys.stdin.readline

# 틀릴 때마다 턱걸이 5회
# 내구도는 상대 계란 무게만큼 깎임
# 깬 후 0보다 작은 경우 계란이 깨짐
N = int(input())
eggs = [list(map(int, input().split())) for _ in range(N)] # 내구도, 무게
ans = 0

# n, 깨진 갯수
def dfs(n, cnt):
  global ans
  if n == N: # 모든 계란을 들고 손에 부딪히기 완료
    ans = max(ans, cnt)
    return
  
  if eggs[n][0] <= 0: # 내가 들고 있는 계란이 깨진 경우
    dfs(n+1, cnt)
  else: # 현재 계란 안깨진 상태
    flag = False # 한번도 안부딪혔다면, 그래도 가야함
    for i in range(N):
      # '나'이거나, 이미 깨진 경우
      if n == i or eggs[i][0] <= 0:
        continue
      # 깬다
      flag = True
      eggs[n][0] -= eggs[i][1]
      eggs[i][0] -= eggs[n][1]
      
      dfs(n+1, cnt + int(eggs[n][0] <= 0) + int(eggs[i][0] <= 0))
      # 원상 복구
      eggs[n][0] += eggs[i][1]
      eggs[i][0] += eggs[n][1]
    if flag == False:
      dfs(n+1, cnt)

dfs(0, 0)
print(ans)