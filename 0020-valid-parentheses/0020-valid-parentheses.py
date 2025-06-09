class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
       
        for st in s:
            if st == '(':
                stack.append('(')
            elif st == '[':
                stack.append('[')
            elif st == '{':
                stack.append('{')
            elif st == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif st == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            elif st == '}':
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True