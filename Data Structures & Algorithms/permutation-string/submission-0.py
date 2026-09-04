class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_count, window_count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            window_count[ord(s2[i]) - ord('a')] += 1
        
        if s1_count == window_count:
            return True
        
        for i in range(len(s1), len(s2)):
            # remove the leftmost character of the window
            left_char = s2[i - len(s1)]
            window_count[ord(left_char) - ord('a')] -= 1

            right_char = s2[i]
            window_count[ord(right_char) - ord('a')] += 1

            if window_count == s1_count:
                return True
        return False