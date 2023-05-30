class Solution:
    def isp(self, n):
        if n<=1:
            return False
        if n==2:
            return True
        for i in range(2,int(sqrt(n)+1)):
            if n%i==0:
                return False
        return True
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        mx = 0
        n = len(nums)
        for i in range(n):
            y = nums[i][i]
            z = nums[i][n-i-1]
            if self.isp(y):
                mx = max(mx, y)
            if self.isp(z):
                mx = max(mx, z)
        return mx


        