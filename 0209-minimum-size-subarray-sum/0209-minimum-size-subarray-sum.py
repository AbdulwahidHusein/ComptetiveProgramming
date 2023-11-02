class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        max_len = float('inf')
        curr_sum = 0
        while right < len(nums):
            if curr_sum >= target:
                print(left, right)
                max_len = min(max_len, right - left)
                while curr_sum >= target:
                    max_len = min(max_len, right - left)
                    curr_sum -= nums[left]
                    left += 1
            curr_sum += nums[right]
            right += 1
        while  left < len(nums):
            if curr_sum >= target:
                max_len = min(max_len, right - left)
            curr_sum -= nums[left]
            left += 1
        return 0 if max_len == float('inf') else max_len