def dfs(numbers, n, total, target):
        global answer
        
        if n == len(numbers) and total == target:
            answer += 1
            return
        # 끝까지 탐색했는데 total 값이 target과 다르다면
        elif n == len(numbers):
            return
        
        dfs(numbers, n+1, total + numbers[n], target)
        dfs(numbers, n+1, total - numbers[n], target)
            
def solution(numbers, target):
    global answer
    answer = 0
    
    dfs(numbers, 0, 0, target)
    return answer