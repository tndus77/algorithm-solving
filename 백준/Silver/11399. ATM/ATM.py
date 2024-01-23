n = int(input())
people = list(map(int, input().split()))
arr = [0]
total = 0

people.sort()

for i in range(len(people)):
  each = arr[i] + people[i]
  arr.append(each)

for x in arr:
  total += x
print(total)
