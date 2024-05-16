import sys
import heapq
input = sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort()

q = []
heapq.heappush(q, lst[0][1])

for i in range(1, N):
  start, end = lst[i]
  
  if start < q[0]: # new 시작 시간 < 끝나는 시간
    heapq.heappush(q, end)
  else: # new 시작 시간 >= 끝나는 시간
    heapq.heappop(q)
    heapq.heappush(q, end)

print(len(q))
