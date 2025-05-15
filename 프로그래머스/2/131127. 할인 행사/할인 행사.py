from collections import Counter
def solution(want, number, discount):
    want_dict = dict(zip(want, number))
    answer = 0
    
    for i in range(len(discount)-9):
        window = discount[i:i+10]
        window_counter = Counter(window)
        match = True
        
        for item in want_dict:
            if  window_counter[item] < want_dict[item]:
                match = False
                break
                
        if match:
            answer += 1
    return answer        
        