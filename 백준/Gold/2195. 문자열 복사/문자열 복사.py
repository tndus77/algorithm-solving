import sys

S = str(input())
P = str(input())
ans = 0

idx = 0
while idx < len(P):
  copy = ''
  if S.find(P[idx:]) != -1: # idx부터 끝까지 답이 있다는 것이니까 이미 끝남
    ans += 1
    break
  for j in range(idx, len(P)):
    copy += P[j]
    if S.find(copy) == -1:
      ans += 1
      idx = j
      break

print(ans)