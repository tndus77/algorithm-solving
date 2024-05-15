N = int(input())

row = [int(input()) for _ in range(N)]

row.sort(reverse=True)

for i in range(N):
  row[i] = row[i] - i
  if row[i] < 1: # 음수라면
    row[i] = 0
print(sum(row))