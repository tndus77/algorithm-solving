from collections import deque

def solution(s):
    answer = True
    lst = list(s)
    q = deque()

    for str in lst:
        if str == '(':
            q.append('(')
        else:
            # q에 값이 있다면
            if q:
                q.pop()
            # 값이 없다면
            else:
                answer = False
                break
    
    if q or answer == False:
        return False
    return True
