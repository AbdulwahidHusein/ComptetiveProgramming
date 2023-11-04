class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        left_sum = [0]*(len(nums)+1)
        right_sum = [0]*(len(nums)+1)

        for i in range(1, len(nums)+1):
            left_sum[i] = left_sum[i-1] + nums[i-1]
        for i in range(len(nums)-1, -1, -1):
            right_sum[i] = right_sum[i+1] + nums[i]
        print(nums, left_sum, right_sum)
        for i in range(len(left_sum)-1):
            if left_sum[i] == right_sum[i+1]:
                return i
        return -1
