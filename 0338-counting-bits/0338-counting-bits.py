class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        ans = []
        for i in range(n+1):
            bin_i = str(bin(i))
            ans.append(bin_i.count("1"))
        return ans
