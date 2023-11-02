class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 2:
            if nums[0] == nums[-1]:
                return 0
            return 2
        pref_poses = {}
        cummulative = 0
        max_size = 0
        for i, n in enumerate(nums):
            if n == 0:
                cummulative -= 1
            else:
                cummulative += 1
            if cummulative == 0:
                max_size = i+1
            if cummulative in pref_poses:
                max_size = max(max_size, i-pref_poses[cummulative])
            else:
                pref_poses[cummulative] = i
        return max_size

