a = int(input())

for i in range(1, a+1):
    if a%10 == 3 or a%10 == 6 or a%10 == 9:
        print('X', end='')
        break
    else:
        print(a, end='')
        break