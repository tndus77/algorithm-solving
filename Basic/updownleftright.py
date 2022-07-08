n = int(input())
plans = input().split()

x, y = 1, 1
step = ['R', 'U', 'L', 'D']

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for plan in plans:
    for i in range(len(step)):
        if plan == step[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        
    #공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    #이동 수행
    x, y = nx, ny

print(x, y)
    