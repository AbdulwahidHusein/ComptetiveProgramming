ts = int(input())
case = 1
for i in range(ts):
    n = int(input())
    arr=[int(i) for i in input().split()]
    high = 0
    low = 0
    for j in range(n-1):
        if arr[j+1]>arr[j]:
            high+=1
        if arr[j+1]<arr[j]:
            low+=1
    print('Case '+str(case)+': ' + str(high)+' '+str(low))
    case+=1
