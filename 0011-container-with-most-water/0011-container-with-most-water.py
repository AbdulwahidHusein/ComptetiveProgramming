class Solution:#greedy
    def maxArea(self, height: List[int]) -> int:
        area = 0
        left, right = 0, len(height)-1
        while left!=right:
            area  = max(area, min(height[left], height[right])*(right-left))
            if height[left]>height[right]:
                right-=1
            else:
                left +=1
        return area
        
