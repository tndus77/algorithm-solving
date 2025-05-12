class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dit = dict()

        if len(s) != len(t):
            return False

        for st in s:
            if st in dit:
                dit[st] += 1
            else:
                dit[st] = 1
        
        for tt in t:
            if tt not in dit:
                return False
            dit[tt] -= 1
        print(dit)
        for dt in dit:
            if dit[dt] != 0:
                return False
        return True