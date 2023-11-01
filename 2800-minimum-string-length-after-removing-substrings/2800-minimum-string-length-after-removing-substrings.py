class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for w in s:
            if stack and w == "B":
                if stack[-1] == "A":
                    stack.pop()
                else:
                    stack.append(w)
            elif stack  and w == "D":
                if stack[-1] == "C":
                    stack.pop()
                else:
                    stack.append(w)
            else:
                stack.append(w)
        print(stack)
        return len(stack)