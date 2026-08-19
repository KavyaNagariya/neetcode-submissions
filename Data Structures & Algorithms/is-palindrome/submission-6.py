class Solution:
    def isPalindrome(self, s: str) -> bool:
        clear = ''
        for c in s:
            if c.lower().isalnum():
                clear += c.lower()
        i, j = 0, len(clear) - 1
        while i <= j:
            if clear[i] == clear[j]:
                i += 1
                j -= 1
            else: 
                return False
        return True

