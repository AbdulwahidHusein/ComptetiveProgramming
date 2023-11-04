class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for l in s:
            if stack and chr(ord(stack[-1])^32) == l:
                stack.pop()
            else:
                stack.append(l)
        return "".join(stack)