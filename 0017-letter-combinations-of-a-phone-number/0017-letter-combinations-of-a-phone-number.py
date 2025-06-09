class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        dictionary = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        def dfs(n, arr):
            nonlocal answer
            if n == len(digits):
                answer.append(''.join(arr))
                return
            
            for num in dictionary[digits[n]]:
                if n+1 <= len(digits):
                    dfs(n+1, arr+[num])
        answer = []
        dfs(0, [])

        return answer