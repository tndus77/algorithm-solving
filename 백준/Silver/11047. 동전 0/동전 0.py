n, k = map(int, input().split())
arr = []

for i in range(n):
  arr.append(input())

sorted(arr)
arr.reverse()

ans = 0

for x in arr:
  if k >= int(x):
    ans += k // int(x)
    k %= int(x)

print(ans)    

