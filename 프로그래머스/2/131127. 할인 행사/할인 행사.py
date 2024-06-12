def solution(want, number, discount):
    from collections import Counter

    answer = 0
    days = 10
    want_dict = dict(zip(want, number))
    
    for start_day in range(len(discount) - days+1):
        current_items = discount[start_day:start_day+days]
        current_counter = Counter(current_items)
        
        isPossible = True
        for item, count in want_dict.items():
            if current_counter[item] < count:
                isPossible = False
        if isPossible:
            answer += 1
    
    
    return answer