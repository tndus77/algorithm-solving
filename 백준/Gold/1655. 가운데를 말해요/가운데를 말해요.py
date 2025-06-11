import sys
import heapq

input = sys.stdin.readline

left_heap = [] # 중간값 이하 저장, 최대힙으로
right_heap = [] # 중간값 이상 저장, 최소힙으로

n = int(input())
for _ in range(n):
  num = int(input())

  heapq.heappush(left_heap, -num)

  if right_heap and right_heap[0] < -left_heap[0]:
    moved = -heapq.heappop(left_heap)
    heapq.heappush(right_heap, moved)
  
  # 왼쪽이 오른쪽보다 같거나, 한 개 많아야한다.
  if len(left_heap) > len(right_heap) + 1:
    moved = -heapq.heappop(left_heap)
    heapq.heappush(right_heap, moved)
  elif len(right_heap) > len(left_heap):
    moved = heapq.heappop(right_heap)
    heapq.heappush(left_heap, -moved)

  print(-left_heap[0])