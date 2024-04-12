from collections import deque

def solution(operations):
    # 큐가 비어있으면 [0, 0]
    # 큐가 비어있지 않으면 [최댓값, 최솟값]
    q = deque()
    answer = []
    
    for item in operations:
        lst = item.split()
        if lst[0] == 'I':
            q.append(int(lst[1]))
        elif lst[0] == 'D':
            if int(lst[1]) < 0:
                # 최솟값 삭제
                if q:
                    q.remove(min(q))
            else:
                if q:
                # 최댓값 삭제
                    q.remove(max(q))
    if q:
        answer.append(max(q))
        answer.append(min(q))
    else:
        answer = [0, 0]
    return answer