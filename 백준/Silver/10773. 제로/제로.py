n = int(input())
arr = []

for i in range(n):
  num = int(input())
  if num == 0:
    arr.pop()
    continue
  arr.append(num)

print(sum(arr))