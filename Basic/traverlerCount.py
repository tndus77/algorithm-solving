n = int(input())
horror = sorted(list(map(int, input().split())))

count = 0 
party = 0 #모험가 수

for i in horror: #공포도 반복문안에서 
    party += 1 # 사람 수랑 같이 증가
    if party >= i: #공포도가 사람수보다 작으면 그룹을 결성할 수 없음
        count += 1 #경우의 수 증가
        party = 0 #사람 수 증가
        
print(count)