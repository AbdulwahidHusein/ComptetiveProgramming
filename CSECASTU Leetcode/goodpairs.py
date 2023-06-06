class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        goodPairs = 0
        for i, num in enumerate(nums):
            for j in range(i+1, len(nums)):
                if num == nums[j]:
                    goodPairs+=1
        return goodPairs