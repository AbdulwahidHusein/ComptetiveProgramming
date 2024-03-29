class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        #towards the median
        nums.sort()
        middle = len(nums)//2-1
        maxs = 0
        for i in range(middle,-1, -1):
            maxs = max(nums[i]+nums[2*middle+1-i], maxs)
        return maxs
