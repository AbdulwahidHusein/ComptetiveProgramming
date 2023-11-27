def number_of_smaller(arr1, arr2):
    ptr1 = 0
    ptr2 = 0
    n1 = len(arr1)
    n2 = len(arr2)
    ans = [0]*n2
    count = 0
    while ptr2 < n2 and ptr1 < n1:
        if arr1[ptr1] >= arr2[ptr2]:
            ans[ptr2] = count
            ptr2 += 1
        else:
            count += 1
            ptr1 += 1
    while ptr2 < n2:
        ans[ptr2] = count
        ptr2 += 1
            
    print( " ".join([str(i) for i in ans]))
    
a, b = map(int, input().split())
arr1 = [int(i) for i in input().split()]
arr2 = [int(i) for i in input().split()]
number_of_smaller(arr1, arr2)
