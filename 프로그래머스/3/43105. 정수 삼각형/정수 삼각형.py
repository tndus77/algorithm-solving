def solution(triangle):
    answer = 0
    dp = [[0] * len(triangle[i]) for i in range(len(triangle))]
    x = len(triangle) # 행
    
    for i in range(1, x):
        for j in range(len(triangle[i])):
            if i == 1:
                dp[i][j] = triangle[0][0] + triangle[i][j]
                continue
            if j == 0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            elif j == i:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
    answer = max(dp[len(triangle)-1])
    return answer