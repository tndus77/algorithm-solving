import sys
from itertools import combinations

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
groups = [x for x in range(N)]
groups = list(combinations(groups, N//2))
ans = 1e9

for group in groups:
  team_A = 0
  team_B = 0
  for i in group:
    for j in group:
      team_A += arr[i][j]
  not_team = [x for x in range(N) if x not in group]
  for i in not_team:
    for j in not_team:
      team_B += arr[i][j]
  
  ans = min(ans, abs(team_A - team_B))

print(ans)