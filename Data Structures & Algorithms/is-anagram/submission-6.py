class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        charCount = {}
        for c in s:
            charCount[c] = charCount.get(c, 0) + 1
        
        for c in t:
            """ #THIS IS PARTICULAR CAN BE REDUCED
            if c not in charCount:
                return False
            if charCount[c] > 0:
                charCount[c] -= 1
                continue
            return False
            """
            #This loop ensures that the charCount should have each char count to zero if its not just return False else True
            if charCount.get(c, 0) == 0: #Checks for missing and exhausted 
                return False
            charCount[c] -= 1
        
        #THIS FOR LOOP NEVER RUNS 
        #for c in charCount.keys():
        #    if charCount[c] == 0:
        #        continue
        #    return False

        return True
        
        

        