import sys
from bisect import bisect_left

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()
questions = [int(input()) for _ in range(M)]

for question in questions:
    idx = bisect_left(arr, question)
    if idx < N and arr[idx] == question:
        print(idx)
    else:
        print(-1)