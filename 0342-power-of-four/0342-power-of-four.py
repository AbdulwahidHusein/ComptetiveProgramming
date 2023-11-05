class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=1:
            if n==1:
                return True
            return False
        return n%4==0 and self.isPowerOfFour(n//4)