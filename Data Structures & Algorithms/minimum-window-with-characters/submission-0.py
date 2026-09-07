class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or len(t) > len(s):
            return ""
        mapT = {}
        for c in t:
            mapT[c] = mapT.get(c, 0) + 1

        required = len(mapT)
        formed, minStart = 0, 0
        window_count = {}
        left, minLen = 0, float('inf')
        for right in range(len(s)):
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1

            if char in mapT and window_count[char] == mapT[char]:
                formed += 1

            while formed == required:
                if right - left + 1 < minLen:
                    minLen = right - left + 1
                    minStart = left
                
                left_char = s[left]
                window_count[left_char] -= 1

                if left_char in mapT and mapT[left_char] > window_count[left_char]:
                    formed -= 1
                
                left += 1
        return "" if minLen == float('inf') else s[minStart: minLen + minStart]