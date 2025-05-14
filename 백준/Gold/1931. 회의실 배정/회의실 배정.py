n = int(input())
meeting_room = []

for _ in range(n):
  meeting_room.append(list(map(int, input().split())))

meeting_room.sort(key=lambda x:(x[1], x[0]))

answer = 0
current_time = 0

for start, end in meeting_room:
  if start >= current_time:
    current_time = end
    answer += 1

print(answer)