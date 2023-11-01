class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = {}
        for l in s:
            if l in counts:
                counts[l] += 1
            else:
                counts[l] = 1
        has_l_1 = 0
        cnt = 0
        for l in counts:
            if counts[l] >=2:
                cnt += 2*(counts[l]//2)
            else:
                has_l_1 = 1
            if counts[l]%2 !=0:
                has_l_1 = 1
        return cnt + has_l_1
        