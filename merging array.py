n1, n2 = map(int, input().split())
arr1 = [int(i) for i in input().split()]
arr2 = [int(i) for i in input().split()]

ptr1 = 0
ptr2 = 0
sa = [0]*(n1+n2)

while ptr1 < n1 and ptr2 < n2:
    if arr1[ptr1] < arr2[ptr2]:
        sa[ptr1+ptr2] = arr1[ptr1]
        ptr1 += 1
    else:
        sa[ptr1+ptr2] = arr2[ptr2]
        ptr2 += 1
while ptr1 < n1:
    sa[ptr1+ptr2] = arr1[ptr1]
    ptr1 += 1
while ptr2 < n2:
    sa[ptr1+ptr2] = arr2[ptr2]
    ptr2 += 1
print(" ".join([str(i) for i in sa]))
