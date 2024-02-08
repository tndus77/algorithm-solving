from collections import deque
def solution(progresses, speeds):
    rest_days = deque()
    
    for i in range(len(progresses)):
        day = 0
        
        need = 100 - progresses[i]
        if need % speeds[i] == 0:
            day = need // speeds[i]
        else:
            day = need // speeds[i] + 1
        rest_days.append(day)
        
    res = []
    
    # 마지막 값보다 작으면 빼지 않고, 크면 빼고, cnt 초기화
    while rest_days:
        temp = rest_days.popleft()
        cnt = 1
        
        while rest_days and temp >= rest_days[0]:
            rest_days.popleft()
            cnt += 1
        res.append(cnt)
    return res