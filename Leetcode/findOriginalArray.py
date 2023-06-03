class Solution:
    def findOriginalArray(self, changed: list[int]) -> list[int]:
        if len(changed)%2!=0:
            return []
        changed.sort()
        ret = []
        if 0 in changed:
            zero = changed.count(0)
            if zero%2!=0:
                return []
        if changed:
            a = changed[0]
            if a==0:
                while changed.count(0)>1:
                    changed.remove(0)
                    changed.remove(0)
                    ret.append(0)
                    if changed:
                        a = changed[0]
                    else:
                        return ret
            while 2*a in changed:
                changed.remove(a)
                changed.remove(2*a)
                ret.append(a)
                if changed:
                    a = changed[0]
                else:
                    return ret
        return []
 
    
s = Solution()
print(s.findOriginalArray([4,0,3,0]))