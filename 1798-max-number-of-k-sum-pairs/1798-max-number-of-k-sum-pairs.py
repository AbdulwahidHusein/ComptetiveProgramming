class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = len(nums)-1
        oprs = 0
        while right > left:
            curr_sum = nums[left] + nums[right] 
            if curr_sum == k:
                oprs += 1
                left += 1
                right -=1
            elif curr_sum > k:
                right -= 1
            else:
                left += 1
        return oprs