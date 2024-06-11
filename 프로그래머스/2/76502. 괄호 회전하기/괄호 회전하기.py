def solution(s):
    answer = 0
    for i in range(len(s)):
        temp_s = s[i:] + s[:i]
        
        while True:
            length = len(temp_s)
            
            temp_s = temp_s.replace("[]", "")
            temp_s = temp_s.replace("{}", "")
            temp_s = temp_s.replace("()", "")
            
            if len(temp_s) == 0: # 모두 소거 완료
                answer += 1
                break
            if length == len(temp_s):
                break
        
    return answer