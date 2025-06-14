import heapq
def solution(n, works):
    heap = []
    
    if n >= sum(works):
        return 0
    
    for work in works:
        heapq.heappush(heap, -work)
    
    while n > 0:
        # 최댓값 삭제
        if heap:
            num = -heapq.heappop(heap)
            if num >= 1:
                heapq.heappush(heap, -(num-1))
        n -= 1
    result = sum([-num * -num for num in heap])
    return result