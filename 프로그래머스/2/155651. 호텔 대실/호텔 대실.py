import heapq

def solution(book_time):
    book_time.sort(key=lambda x:x[0])
    heap = []
    minNum = 0
    
    for start, end in book_time:
        if heap and heap[0] <= 60 * int(start[:2]) + int(start[3:]): # 객실 change
            heapq.heappop(heap) # 최솟값 삭제
        heapq.heappush(heap, 60 * int(end[:2]) + int(end[3:]) + 10)
    
    return len(heap)