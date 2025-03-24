from itertools import permutations
def solution(numbers):
    answer = 0
    
    def isPrime(n):
        if n < 2: return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                # 나누어 떨어지는게 있으면
                return False
        return True
    
    unique_numbers = set()
    
    for i in range(1, len(numbers)+1):
        for perm in permutations(numbers, i):
            num = int(''.join(perm))
            unique_numbers.add(num)
    
    for num in unique_numbers:
        if isPrime(num):
            answer += 1
        
    return answer