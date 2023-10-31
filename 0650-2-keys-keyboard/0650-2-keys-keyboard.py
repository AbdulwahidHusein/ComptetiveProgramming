class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        
        def numop(n):
            if n == 1:
                return 0
            
            # Check if n is divisible by any number from 2 to n-1
            for i in range(2, n):
                if n % i == 0:
                    # If n is divisible, perform a copy all operation and then paste n/i times
                    return i + numop(n // i)
            
            # If n is not divisible, perform a copy all operation and then paste once
            return n
        
        return numop(n)