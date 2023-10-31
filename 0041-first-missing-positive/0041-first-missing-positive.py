class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        missing_nums = 0
        l = len(nums)
        for i in range(l):
            if nums[i] <= l and nums[i] > 0:
                if i+1 != nums[i]:
                    temp = nums[nums[i]-1]
                    nums[nums[i]-1] = nums[i]
                    nums[i] = temp
        for i in range(l):
            if nums[i] <= l and nums[i] > 0:
                if i+1 != nums[i]:
                    temp = nums[nums[i]-1]
                    nums[nums[i]-1] = nums[i]
                    nums[i] = temp
        for i in range(l):
            if nums[i] <= l and nums[i] > 0:
                if i+1 != nums[i]:
                    temp = nums[nums[i]-1]
                    nums[nums[i]-1] = nums[i]
                    nums[i] = temp
        for i in range(l):
            if nums[i] <= l and nums[i] > 0:
                if i+1 != nums[i]:
                    temp = nums[nums[i]-1]
                    nums[nums[i]-1] = nums[i]
                    nums[i] = temp
        for i in range(l):
            if nums[i] <= l and nums[i] > 0:
                if i+1 != nums[i]:
                    temp = nums[nums[i]-1]
                    nums[nums[i]-1] = nums[i]
                    nums[i] = temp

        #remove zeros
        print(nums)
        left = -1
        right = 0
        if nums[0] <0 or nums[0] >l:
            left =0
            right = 1
        while right < len(nums):
            if nums[right] <l and nums[right > 0]:
                if left >= 0:
                    nums[left] = nums[right]
                    left +=1
            right += 1


        print(nums)
        for i in range(l):
            if nums[i] != i+1:
                return i+1
        return l+1