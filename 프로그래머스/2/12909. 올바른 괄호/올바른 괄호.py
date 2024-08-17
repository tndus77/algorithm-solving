from collections import deque
def solution(s):
    answer = True
    q = deque()
    
    for str in s:
        if str == "(":
            q.append("(")
        if str == ")":
            if q:
                q.popleft()
            else:
                answer = False
    
    if q:
        answer = False
    return answer