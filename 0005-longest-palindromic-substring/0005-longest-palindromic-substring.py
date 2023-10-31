class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        max_str = ""
        max_l = 1
        dp = [[False for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            max_str = s[i]
        
        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    if dp[i+1][j-1] or i==j-1:
                        dp[i][j] = True
                        if j-i+1 > max_l:
                            max_l = j-i+1
                            max_str = s[i:j+1]
        return max_str


