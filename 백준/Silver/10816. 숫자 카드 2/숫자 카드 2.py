import sys
import bisect

n = int(input())
have = list(map(int, input().split()))
have.sort()
m = int(input())
cards = list(map(int, input().split()))
answer = []

for card in cards:
    start_idx = bisect.bisect_left(have, card)
    end_idx = bisect.bisect(have, card)

    # 있으면
    if start_idx < n and have[start_idx] == card:
        if start_idx != end_idx:
            answer.append(end_idx - start_idx)
        else:
            answer.append(1)
    # 없으면
    else:
        answer.append(0)
print(' '.join(map(str, answer)))