input_data = input()#열 행 표현
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1
count = 0

steps = [(2, -1), (2, 1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

for step in steps: 
    next_column = column + step[1]
    next_row = row + step[0] #이동할 위치 
    
    if next_row < 1 or next_column < 1 or next_row > 8 or next_column > 8 :
        continue
    count += 1
    
print(count)