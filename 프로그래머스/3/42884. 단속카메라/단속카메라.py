def solution(routes):
    # 고속도로에 진입한 지점, 고속도로에서 나간 지점
    
    routes.sort(key=lambda x:x[1])
    answer = 0      

    camera = -30001
    
    for route in routes:
        if camera < route[0]:
            camera = route[1]
            answer += 1
    return answer