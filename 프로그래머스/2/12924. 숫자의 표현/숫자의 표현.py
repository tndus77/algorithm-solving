def solution(n):
    answer = 0
    
    for num in range(1,n+1):
        total = 0
        while total < n:
            total += num
            if total == n:
                answer += 1
                break
            num += 1
    return answer