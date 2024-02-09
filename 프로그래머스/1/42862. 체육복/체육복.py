def solution(n, lost, reserve):
    answer = 0
    
    # lost 값도 빼줘야 한다.
    _lost = set(lost) - set(reserve)
    _reserve = set(reserve) - set(lost)
    
    for item in _lost:
        if item-1 in _reserve:
            reserve.remove(item-1)
        elif item+1 in _reserve:
            _reserve.remove(item+1)
        else: # 없으면
            n -= 1
    
    return n