import sys

input = sys.stdin.readline().strip()
stack = [] #총 막대기 갯수
result = 0 #막대기가 쪼개진 갯수 

for i in range(len(input)):
    #'('이 나올 경우 stack에 push
    if input[i] == '(':
        stack.append('(')
        
    else: #')'이 올경우
        #')' 전에 '('가 나올 경우 stack에서 pop하고 stack의 길이만큼 result에 더하기
        if input[i-1] == '(':
            stack.pop()
            result += len(stack)
        #')'전에 ')' 올 경우 
        else:
            stack.pop() #막대기 한개 끝
            result += 1
            
print(result)