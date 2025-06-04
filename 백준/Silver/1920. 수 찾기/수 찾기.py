import sys
import bisect

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = int(input())
search = list(map(int, input().split()))

for i in range(m):
    idx = bisect.bisect_left(arr, search[i])
    if idx < n and arr[idx] == search[i]:
        print(1)
    else:
        print(0)