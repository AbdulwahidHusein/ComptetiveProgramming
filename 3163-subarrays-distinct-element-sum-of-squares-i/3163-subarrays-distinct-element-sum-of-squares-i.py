class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                s = set()
                a = i
                while a <=j:
                    s.add(nums[a])
                    a+=1
                print(list(s))
                ans += len(s)*len(s)
        return ans