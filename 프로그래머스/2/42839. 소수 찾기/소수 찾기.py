from itertools import *

def solution(numbers):
    # 글자로 만들 수 있는 경우의 수를 모두 찾아서 arr에 넣자.
    # 소수인지 확인만 해주면 된다.
    arr = list(numbers)
    result = []
    answer = []
    
    for i in range(1, len(numbers)+1):
        result += permutations(arr, i)
    new_nums = [int(("").join(p)) for p in result]
    
    def isPrime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    
    for item in new_nums:
        if isPrime(int(item)):
            answer.append(int(item))
    
    return len(set(answer))