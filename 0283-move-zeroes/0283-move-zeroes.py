class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        right = 0
        while right < len(nums):
            if nums[right] == 0:
                pass
            else:
                nums[left] = nums[right]
                left += 1
            right+=1
        while left < len(nums):
            nums[left] = 0
            left += 1
            





        """
        Do not return anything, modify nums in-place instead.
        """
        