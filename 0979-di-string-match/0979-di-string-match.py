class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        perms = []
        n = len(s)
        initial = 0
        used = [0]*(n+1)
        for l in s:
            if l == "I":
                perms.append(initial)
                used[initial] = 1
                initial += 1
            else:
                perms.append(n)
                used[n] = 1
                n-=1
        for i in range(len(used)):
            if used[i]==0:
                perms.append(i)
        return perms