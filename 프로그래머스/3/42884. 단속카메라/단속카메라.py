def solution(routes):
    answer = 0
    target = -30000
    routes.sort(key=lambda x:x[1])
    
    for route in routes:
        [start, end] = route
        if start > target:
            target = end
            answer += 1
    return answer