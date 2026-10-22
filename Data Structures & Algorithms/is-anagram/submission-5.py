class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        charCount = {}
        for c in s:
            charCount[c] = charCount.get(c, 0) + 1
        
        for c in t:
            if c not in charCount:
                return False
            if charCount[c] > 0:
                charCount[c] -= 1
                continue
            return False
        
        for c in charCount.keys():
            if charCount[c] == 0:
                continue
            return False

        return True
        
        

        