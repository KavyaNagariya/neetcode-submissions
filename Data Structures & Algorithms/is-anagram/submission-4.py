class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sortS, sortT = {}, {}
        for i in range(len(s)):
            sortS[s[i]] = 1 + sortS.get(s[i], 0)
            sortT[t[i]] = 1 + sortT.get(t[i], 0)
        for c in sortS:
            if sortS[c] != sortT.get(c , 0):
                return False
        
        return True