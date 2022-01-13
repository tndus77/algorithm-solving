import heapq
import sys

n = int(input())
list = []

for i in range(n):
    x = int(input())
    heapq.heapify(list)
    
    if x != 0 :
        heapq.heappush(list, (abs(x), x))  #리스트에 x를 넣음
    else:
        if len(list) == 0:
            print(0)
        else:
            print(heapq.heappop(list)[1])
            
        