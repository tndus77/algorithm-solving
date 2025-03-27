from itertools import permutations

def solution(number, k):
    answer = ''
    stack = []
    stack.append(number[0])
    
    for i in range(1, len(number)):
        while stack and stack[-1] < number[i] and k > 0:
            k -= 1
            stack.pop()
        stack.append(number[i])
    stack = stack[:len(stack)-k]
    
    return ''.join(map(str, stack))