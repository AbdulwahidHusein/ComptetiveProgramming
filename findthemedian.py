from collections import deque
arr = deque()
instr = input()
while True:
    try:
        if ' ' in instr:
            r, n = instr.split()
            n = int(n.strip())
            arr.appendleft(n)
        elif instr.strip()=='REMOVE':
            print(arr.pop())
        else:
            arr = deque()
        instr = input()
    except:
        break