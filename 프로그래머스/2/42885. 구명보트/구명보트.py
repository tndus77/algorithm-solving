from collections import deque
def solution(people, limit):
    answer = 0
    
    people.sort()
    q = deque(people)
    
    while len(q) > 1:
        if q[0] + q[-1] <= limit: # 최소값과 최댓값이 limit보다 작으면
            q.popleft()
            q.pop()
        else: # limit보다 크면 최댓값 빼기
            q.pop()
        answer += 1
    
    if q: #1명 남아 있을 때
        answer += 1
            
    
    return answer