n = int(input())
case = 1
for i in range(n):
    d  = int(input())
    flag = True
    arr = []
    for i in range(d):
        arr.append([i for i in input().split()])
    for j in range(d):
        s =''
        for k in range(d):
            s+=arr[k][j]
        if len(s)!=len(set(s)):
            flag = False
    if flag:
        print('Case '+ str(case) +': yes')
        case+=1
    else:
        print('Case '+ str(case) +': no')
        case+=1
        