# 중복되는 값을 찾으려면 set()을 이용하자!
n, m = map(int, input().split())
heardArr = set()
seeArr = set()

for i in range(n):
  heardArr.add(input())

for i in range(m):
  seeArr.add(input())

result = sorted(heardArr & seeArr)

print(len(result))
for x in result:
  print(x)
