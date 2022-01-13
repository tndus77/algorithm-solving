import sys

input = sys.stdin.readline().strip()
stack = []
#1. 피연산자면 queue에 append
#2. 
for i in input:
    if i.isalpha(): #피연산자이면
        print(i, end='')
    #연산자면 stack에 넣기
    else:
        #연산자 우선순위 비교
        if i == "(":
            stack.append(i)
        elif i == '*' or i == '/':
            stack.append(i)
        elif i == '+' or i == '/':
            if stack[-1] == "*" or stack[-1] == "/":
                print(stack.pop(), end='')
            stack.append(i)
        elif i == ")":
            while stack[-1] != "(":
                print(stack.pop())
            stack.pop()
            
        
        