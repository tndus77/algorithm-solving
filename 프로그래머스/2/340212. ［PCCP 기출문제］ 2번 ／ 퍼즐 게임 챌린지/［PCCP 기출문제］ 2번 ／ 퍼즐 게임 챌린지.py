def solution(diffs, times, limit):
    def obtain_limit(level):
        total = 0
        for i in range(len(diffs)):
            if diffs[i] > level:
                if i == 0:
                    total += times[i]
                else:
                    error = diffs[i] - level
                    total += (times[i-1] + times[i]) * error + times[i]
            else:
                total += times[i]
        return total
    
    # level이 커질수록 limit이 작아짐. 이진 탐색 사용
    left, right = 0, max(diffs)
    answer = 0
    
    while left <= right:
        mid = (left + right) // 2
        if obtain_limit(mid) <= limit:
            answer = mid
            right = mid - 1
        else: # obtain_limit(mid) > limit
            left = mid + 1
    if answer == 0:
        return 1
    return answer