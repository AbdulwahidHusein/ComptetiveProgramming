class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        triplets =[]

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)-2):
                start = j+1
                end = len(nums)-1
                while start < end:
                    cand = [nums[i], nums[j], nums[start], nums[end]]

                    s = sum(cand)
                    if s == target and not cand in triplets:
                        triplets.append(cand)
                        start += 1
                        end -=1
                    elif s < target:
                        start += 1
                    else:
                        end -= 1
        return triplets