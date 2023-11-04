class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        fib  = 0
        lower = 0
        upper = 1
        for i in range(2, n):
            temp = lower
            lower = upper
            upper = upper + temp

        return lower + upper