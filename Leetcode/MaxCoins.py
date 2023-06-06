#link  https://leetcode.com/problems/maximum-number-of-coins-you-can-get/
class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        #top2s must be as close as possible
        #the third should be as least as possible -> greedy algorithm
        piles.sort()
        leng = len(piles)
        lefti = piles[leng//3:]
        summ = 0
        for i, n in enumerate(lefti):
            if i%2==0:
                summ+=n
        return summ
        #[1,2,|3,4,5,6,7,8,9]1,2,3,|4,5,6,7,8,9