sugar = int(input())
count = 0

while sugar >= 0:
  if sugar % 5 == 0: # 5의 배수이면
    count += sugar // 5
    sugar %= 5
    break
  sugar -= 3
  count += 1
else:
  count = -1

print(count)