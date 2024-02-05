from collections import Counter
word = list(map(str, input()))
word.sort()
check = Counter(word)

cnt = 0 # 홀수 등장 갯수
center = "" # 홀수 문자

res = ""

for i in check:
  # 문자의 갯수가 홀수인 경우
  if check[i] % 2 != 0:
    cnt += 1
    center += i
    word.remove(i)
  
  if cnt > 1:
    break

if cnt > 1:
  print("I'm Sorry Hansoo")
else:
  for i in range(0, len(word), 2):
    res += word[i]
  print(res+center+res[::-1])

  