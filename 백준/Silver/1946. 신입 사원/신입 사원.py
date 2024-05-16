import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
  M = int(input())
  a = [list(map(int, input().split())) for _ in range(M)]
  a.sort()

  L = a[0][1] # 이미 서류는 1등. 따라서 면접은 꼴찌여도 상관없음
  stack = [L]

  for i in range(1, M):
    if a[i][1] < L: # 이것보다 무조건 작아야 선발!
      L = a[i][1]
      stack.append(a[i][1])

  print(len(stack))