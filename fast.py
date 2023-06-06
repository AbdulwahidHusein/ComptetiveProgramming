n, x = [int(i) for i in input().split()]
arr = [int(j) for j in input().split()]
sums = []
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i]+arr[j]==x:
            lst = [arr[i],arr[j]]
            lst.sort()
            sums.append(lst)
if len(sums)==0:
    print('impossible')
else:
    s = min(sums)
    print(str(s[0][0])+' '+str(s[0][1]))
