class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        #-11 2 3 4 5 6 7 8
        #0 -11 -9 
        nums.sort()
        pref_sum = [0]
        for n in nums:
            pref_sum.append(pref_sum[-1] + n)
        right_sum = 0
        for i in range(len(nums), 0, -1):
            right_sum += nums[i-1]
            if right_sum > pref_sum[i-1]:
                ret = nums[i-1:]
                ret.reverse()
                return ret
        