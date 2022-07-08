import heapq
import sys

n = int(input())
heap = []

for i in range(n):
    num = int(sys.stdin.readline())
    
    if num > 0:
        heapq.heappush(heap, (-num,num))
    else: #num == 0
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])