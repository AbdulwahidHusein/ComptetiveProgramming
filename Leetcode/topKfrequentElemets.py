#https://leetcode.com/problems/top-k-frequent-elements/
from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        dictt = Counter(nums)
        mostk = dictt.most_common(k)
        arr = []
        for a,b in mostk:
            arr.append(a)
        return arr
