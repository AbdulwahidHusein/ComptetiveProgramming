class Solution:
    def isValid(self, s: str) -> bool:
        opr = 0
        oabr = 0
        ocb = 0
        tobec = []
        for c in s:
            if c == '(':
                opr += 1
                tobec.append(')')
            elif c == '[':
                oabr += 1
                tobec.append(']')
            elif c == '{':
                ocb += 1
                tobec.append('}')
            elif c == ')':
                opr -= 1
                if not tobec:
                    return False
                if tobec.pop() != ')':
                    return False
            elif c == ']':
                oabr -= 1
                if not tobec:
                    return False
                if tobec.pop()!= ']':
                    return False
            elif c == '}':
                ocb -= 1
                if not tobec:
                    return False
                if tobec.pop()!= '}':
                    return False
        return opr==0 and oabr==0 and ocb==0
        