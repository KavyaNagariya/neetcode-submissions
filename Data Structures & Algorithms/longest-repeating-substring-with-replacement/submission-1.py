class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freq = [0] * 26
        maxFreq = 0
        maxWindow = 0
        for r in range(len(s)):
            freq[ord(s[r]) - ord('A')] += 1
            maxFreq = max(maxFreq, freq[ord(s[r]) - ord('A')])
            window = r - l + 1
            # Window - maxFreq give us the characters needed to change.
            if window - maxFreq > k:
                freq[ord(s[l]) - ord('A')] -= 1
                l += 1
            window = r - l + 1
            maxWindow = max(maxWindow, window)
        return maxWindow