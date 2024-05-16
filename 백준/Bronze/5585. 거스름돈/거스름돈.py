charge = int(input())
change = 1000 - charge
cnt = 0

while change > 0:
  if change >= 100:
    fi = change // 100
    if fi >= 5:
      change -= 500
    else:
      change -= 100
    cnt += 1
  elif change >= 10:
    fi = change // 10
    if fi >= 5:
      change -= 50
    else:
      change -= 10
    cnt += 1
  else:
    fi = change % 10
    if fi >= 5:
      change -= 5
    else:
      change -= 1
    cnt += 1
print(cnt)