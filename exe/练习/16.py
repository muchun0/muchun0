'''使用列表推导式求列表中每个奇数的平方。 该列表由逗号分隔的数字序列输入。 假设向程序提供了以下输入:  '''
aList = [1,2,3,4,5,6,7,8,9]
b = []
for i in aList:
    if i % 2 != 0:
        j = i ** 2
        j = str(j)
        b.append(j)
    else:
        continue
print(','.join(b))