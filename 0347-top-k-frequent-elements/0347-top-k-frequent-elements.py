from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictt = Counter(nums)
        mostk = dictt.most_common(k)
        arr = []
        for a,b in mostk:
            arr.append(a)
        return arr
