def findDigit(index):
    if index<=45:
        Lgroup = int(0.5 + ((8*index+1)**0.5)/2)-1
        Lval = int((Lgroup*Lgroup + Lgroup)/2)
        leng_required = index - Lval
        if leng_required>0:
            if leng_required<=9:
                return leng_required
        return Lgroup
    if index<=9045:#gg99
        Lgroup = 4 + int((index-20)**0.5)
        Lval = Lgroup*Lgroup - 8*Lgroup +36
        leng_required = index-Lval
        strr = ''
        print(leng_required,'wer')
        for i in range(Lgroup+2):
            strr = ''.join([str(j) for j in range(1, i)])
        return strr[leng_required]
    if index<=1395495:#g999
        Lgroup = int((213/2 + ((213/2)**2+(index-4887))**0.5)/3)
        Lval = int(4887 + 3*Lgroup*Lgroup/2 -213*Lgroup/2)
        leng_required = index-Lval
        if leng_required<=9:
            return leng_required
        if leng_required<=189:#two digit
            num = (leng_required+9)/2
            if num-int(num)>0:
                num = int(num+1)#round up and return
                return int(num/10)
            else:
                return int(num%10)
        if leng_required<=2289:#3 digit
            num = (leng_required+108)/3
            if num-int(num)>0:
                num = int(num+1)#round up and return
                return int(num/100)
            else:
                return int(num%100)
    if index<=189414495:#fourdigit
        Lgroup = int(276.25 + ((8*index - 2806079)**0.5)/4)
        Lval = int(2*Lgroup*Lgroup - 1105*Lgroup + 503388)
        leng_required = index-Lval
        if leng_required<=9:
            return leng_required
        if leng_required<=189:#two digit
            num = (leng_required+9)/2
            if num-int(num)>0:
                num = int(num+1)#round up and return
                return int(num/10)
            else:
                return int(num%10)
        if leng_required<=2889:#3 digit
            num = (leng_required+108)/3
            if num-int(num)>0:
                num = int(num+1)#round up and return
                return int(num/100)
            else:
                return int(num%100)
        if leng_required<=38885:#four digit
            (leng_required+1107)/4
            if num-int(num)>0:
                num = int(num+1)#round up and return
                return int(num/1000)
            else:
                return int(num%1000)
for i in range(1,3000):
    print(str(findDigit(i)), end=" ")