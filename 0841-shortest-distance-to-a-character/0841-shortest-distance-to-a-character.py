class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        left_dis = [float('inf')]*n
        right_dis = [float('inf')]*n

        left = 0
        last_ind = -float('inf')
        right = n-1
        while left < n:
            if s[left] == c:
                left_dis[left] = 0
                last_ind = left
            else:
                left_dis[left] = left - last_ind
            left += 1
        last_ind = float('inf')
        while right > -1:
            if s[right] == c:
                right_dis[right] = 0
                last_ind = right
            else:
                right_dis[right] = last_ind - right
            right -= 1
            
        for i in range(n):
            left_dis[i] = min(left_dis[i], right_dis[i])
        return left_dis