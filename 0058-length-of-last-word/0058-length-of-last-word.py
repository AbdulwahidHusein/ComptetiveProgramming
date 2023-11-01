class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        
        count = 0
        right = len(s) - 1
        while s[right] != " ":
            count += 1
            right -=1
            if right < 0:
                break
        return count
        