n = int(input())

for i in range(n):
    arr = [int(i) for i in input().split()]
    esc = True
    for i in range(len(arr)-1):
        if arr[i]+1 !=arr[i+1]:
            esc = False
    if esc:
        print('Y')
    else:
        print('N')