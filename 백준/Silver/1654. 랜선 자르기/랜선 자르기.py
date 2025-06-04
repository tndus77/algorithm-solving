import sys

K, N = map(int, input().split())
lines = [int(input()) for _ in range(K)]

start, end = 1, max(lines)
result = 0

while start <= end:
    answer = 0
    mid = (start + end) // 2
    
    for i in range(K):
        if (lines[i] // mid) > 0:
            answer += lines[i] // mid
    
    if answer >= N:
        # 남아돈다!
        result = mid # 가능한 길이 중 하나, 더 길게 시도!
        start = mid + 1
    else:
        # 더 잘게 잘라야한다.
        end = mid - 1
print(result)