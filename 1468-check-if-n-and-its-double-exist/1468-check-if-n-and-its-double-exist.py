class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        poss = {}
        for i, n in enumerate(arr):
            if n % 2 == 0 and n//2 in poss:
                return True
            if 2*n in poss:
                return True
            poss[n] = i
        return False
            
            