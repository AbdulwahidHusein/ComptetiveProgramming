class Solution:
    def sortColors(self, nums: list[int]) -> None:
        sortedC = []
        zeros = nums.count(0)
        ones = nums.count(1)
        twos = nums.count(2)
        i =0
        while i<zeros:
            sortedC.append(0)
            i+=1
        i=0
        while i<ones:
            sortedC.append(1)
            i+=1
        i=0
        while i<twos:
            sortedC.append(2)
            i+=1
        return sortedC
s = Solution()

print(s.sortColors([2, 2,1,1,1,0,0,1,0]))