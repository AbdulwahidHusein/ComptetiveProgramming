
def isp(n):
    if n<=1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

n = int(input())
while True:
    if n==-1:
        break
    if isp(n):
        print(str(n)+' is PRIME!!')
    else:
        print(str(n)+" is COMPOSITE TT")
    n = int(input())