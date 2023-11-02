class Solution:
    def numberOfSteps(self, num: int) -> int:
        
        def minn(n):
            if n==0:
                return 0
            if n%2 == 0:
                return 1 + minn(n//2)
            else:
                return 1 + minn(n-1)
        return minn(num)
        