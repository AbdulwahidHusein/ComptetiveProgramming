class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        def traverse(candid, arr,sm):               
            if sm == target: 
                self.ans.append(arr)
                return
            if sm >= target: 
                return   
            for i in range(len(candid)):
                traverse(candid[i:], arr + [candid[i]], sm+candid[i])
        traverse(candidates,[], 0)
        return self.ans