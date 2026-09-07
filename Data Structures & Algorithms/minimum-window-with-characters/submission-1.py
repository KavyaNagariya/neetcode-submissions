class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ""
        
        # Frequency map for characters in t
        mapT = {}
        for c in t:
            mapT[c] = mapT.get(c, 0) + 1
        
        required = len(mapT)          # Number of unique chars in t
        formed = 0                    # How many unique chars are satisfied
        window_counts = {}            # Frequency map for current window
        
        left = 0
        minLen = float('inf')
        minStart = 0
        
        for right in range(len(s)):
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1
            
            # Check if this char satisfies a requirement from t
            if char in mapT and window_counts[char] == mapT[char]:
                formed += 1
            
            # Try to shrink from left while window is valid
            while formed == required:
                # Update minimum window
                if right - left + 1 < minLen:
                    minLen = right - left + 1
                    minStart = left
                
                # Remove left char from window
                left_char = s[left]
                window_counts[left_char] -= 1
                
                # Check if removing this broke a requirement
                if left_char in mapT and window_counts[left_char] < mapT[left_char]:
                    formed -= 1
                
                left += 1
        
        return "" if minLen == float('inf') else s[minStart : minStart + minLen]