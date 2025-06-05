import sys
from collections import Counter

N, M = map(int, input().split())
words = [sys.stdin.readline().strip() for _ in range(N)]
counter = Counter(word for word in words if len(word) >= M)

sorted_counter = sorted(counter.items(), key=lambda x:(-x[1], -len(x[0]), x[0]))

for word, _ in sorted_counter:
    print(word)