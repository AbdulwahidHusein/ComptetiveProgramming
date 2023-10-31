class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums)-2):
            if i+2 >= len(nums):
                return len(nums)
            while  nums[i+2] == nums[i]:
                nums.remove(nums[i])
                if i+2 >= len(nums):
                    return len(nums)
        return len(nums)