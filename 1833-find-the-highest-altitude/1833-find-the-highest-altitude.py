class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_height = 0
        pref_sum = 0
        for i in range(len(gain)):
            pref_sum += gain[i]
            max_height = max(max_height, pref_sum)
        return max_height
