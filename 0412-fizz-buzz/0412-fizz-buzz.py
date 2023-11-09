class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = [0]*n
        for i in range(1,n+1):
            mod3, mod5 = i%3, i%5
            if mod3==0 and mod5 == 0:
                ans[i-1] = "FizzBuzz"
            elif mod3==0:
                ans[i-1] = "Fizz"
            elif mod5==0:
                ans[i-1] = "Buzz"
            else:
                ans[i-1] = f"{i}"
        return ans