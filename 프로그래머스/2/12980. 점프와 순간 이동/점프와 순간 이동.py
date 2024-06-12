def solution(n):
    ans = 0
    
    while n > 0:
        while n % 2 != 0: # 짝수가 아니면
            n -= 1
            ans += 1
        n //= 2
    return ans