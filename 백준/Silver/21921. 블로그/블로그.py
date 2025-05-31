import sys

input = sys.stdin.readline

N, X = map(int, input().split())
viewers = list(map(int, input().split()))
current_sum = sum(viewers[:X])
max_sum = current_sum
cnt = 1

for i in range(X, N):
    current_sum = current_sum - viewers[i-X] + viewers[i]
    
    if current_sum > max_sum:
        max_sum = current_sum
        cnt = 1
    elif current_sum == max_sum:
        cnt += 1

if max_sum == 0:
    print('SAD')
else:
    print(max_sum)
    print(cnt)