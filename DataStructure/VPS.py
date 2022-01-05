t = int(input())

for i in range(t):
    command = input()
    list = []
    
    for j in command:
        if j == '(':
            list.append(j)
        elif j == ')':
            if len(list) != 0 and list[-1] == '(':
                list.pop()
            else:
                list.append(j)
                break
    
    if len(list) == 0:
        print('YES')
    else:
        print('NO')   