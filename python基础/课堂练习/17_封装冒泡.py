def paopao(alist):
    for i in range(len(alist)-1):
        for j in range(len(alist)-1 -i):
            if alist[j] > alist[j+1]:
                alist[j],alist[j+1] = alist[j+1],alist[j]
    else:
        return alist
list1 = [1,3,8,4,5]
print(paopao(list1))
list2 = [6,6,23,6,2343,6324]
print(paopao(list2))