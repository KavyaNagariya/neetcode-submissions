class Solution:
    def isPalindrome(self, s: str) -> bool:
        clear = ''
        for c in s:
            if c.lower().isalnum():
                clear += c.lower()
        reverse = clear[::-1]
        if clear == reverse:
            return True
        return False

