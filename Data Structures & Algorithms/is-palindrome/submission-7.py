class Solution:
    def isPalindrome(self, s: str) -> bool:
        #first store it in a fresh string to compare without any punctuation marks 
        fresh = ""
        for c in s.lower():
            if c.isalnum():
                fresh += c
        
        return fresh == fresh[::-1]