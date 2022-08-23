'''编写一个程序，找出1000到3000之间的所有数字(包括这两个数字)，
使这个数字的每个数字都是偶数。 获得的数字应以逗号分隔的序列打印在单行上。  '''
a = []
for i in range(1000,3001):
    i = str(i)
    c = 1
    for j in range(len(i)):
        j = int(i[j])
        if j % 2 != 0:
            c = 0
    if c == 1:
        a.append(i)
else:
    print(','.join(a))
