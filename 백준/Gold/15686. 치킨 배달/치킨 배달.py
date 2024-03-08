from itertools import combinations

# n 도시 정보, M 폐업시키지 않을 치킨집
# 치킨 거리 = 집과 가장 가까운 치킨집 사이의 거리
# 출력: 도시의 치킨 거리의 최솟값 = 모든 집의 치킨 거리

N, M = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]
house = [] # 집의 좌표
chicken = [] # 치킨 집의 좌표
result = 999999

for i in range(N):
  for j in range(N):
    if area[i][j] == 1:
      house.append([i, j])
    elif area[i][j] == 2:
      chicken.append([i, j])

for ch in combinations(chicken, M): # M개의 조합으로 치킨집 선택
  total = 0
  for h in house:
    min_num = float('inf')
    for c in ch:
      min_num = min(min_num, abs(c[0] - h[0]) + abs(c[1] - h[1]))
    total += min_num
  result = min(result, total)

print(result)