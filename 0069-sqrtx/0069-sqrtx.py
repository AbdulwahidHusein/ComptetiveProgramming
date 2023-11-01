class Solution:
    def mySqrt(self, x: int) -> int:
        if x ==0:
            return 0
        if x ==1 or x ==2 or x==3:
            return 1

        for i in range(x//2+2):
            if i*i > x:
                return i-1
            elif i*i == x:
                return i
                 
        