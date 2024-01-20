n = int(input())
aArr = list(map(int, input().split()))
bArr = list(map(int, input().split()))

# A는 재배열 가능, B는 재배열 불가.
# S의 값을 가장 작게 만들기 위해 A의 수를 재배열 하자.
# B의 가장 큰 수와 A의 가장 작은 수가 만나야하고, B의 가장 작은 수와 A의 가장 큰 수가 만나야 한다.

s = 0

for i in range(n):
  s += min(aArr) * max(bArr)
  aArr.remove(min(aArr))
  bArr.remove(max(bArr))

print(s)

