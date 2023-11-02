class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_sofar = float('inf')
        pref_sum = 0
        for i in range(len(nums)):
            pref_sum += nums[i]
            min_sofar = min(min_sofar, pref_sum)
        if min_sofar > 0:
            return 1
        return 1-min_sofar
        

        