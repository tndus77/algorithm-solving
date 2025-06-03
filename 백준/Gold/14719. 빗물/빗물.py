import sys

input = sys.stdin.readline
H, W = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

for i in range(1, W-1):
    left_max = max(arr[:i])
    right_max = max(arr[i+1:])

    compare = min(left_max, right_max)

    if compare > arr[i]:
        ans += compare - arr[i]

print(ans)