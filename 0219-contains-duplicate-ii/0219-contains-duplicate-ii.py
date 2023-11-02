class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        positions = {}

        for i, n in enumerate(nums):
            if n in positions and i-positions[n] <= k:
                return True
            positions[n] = i
        return False
        