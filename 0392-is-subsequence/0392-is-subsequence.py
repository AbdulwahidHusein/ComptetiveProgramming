class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s=="":
            return True
        if t=="":
            return s==""
        if len(t) == 1:
            return s==t
        
        dp = [[False for _ in range(len(s)+1)] for _ in range(len(t)+1)]

        dp[0][0] = True
        for j in range(1, len(t)+1):
            dp[j][0] = True
        for i in range(1, len(s)+1):
            dp[0][i] = False
        
        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                if s[i-1] == t[j-1]:
                    dp[j][i] = dp[j-1][i-1]
                else:
                    dp[j][i] = dp[j-1][i]
        print(dp)
        return dp[-1][-1]