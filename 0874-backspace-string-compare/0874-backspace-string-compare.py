class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []

        for w in s:
            if w == "#":
                if stack1:
                    stack1.pop()
            else:
                stack1.append(w)
        for r in t:
            if r == "#":
                if stack2:
                    stack2.pop()
            else:
                stack2.append(r)
        print(stack1, stack2)
        return stack1 == stack2
        
        