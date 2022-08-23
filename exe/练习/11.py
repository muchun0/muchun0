'''编写一个程序，接受一个逗号分隔的4位二进制数序列作为输入，然后检查它们是否能被5整除。 能被5整除的数将以逗号分隔的顺序输出。 '''
a = input('请输入需要判断的数').split(',')
b = []
for i in a:
    i = int(i)
    if i % 5 == 0:
        b.append(i)
else:
        if len(b) == 1:
            print(b[0])
        else:
            print(','.join(b))
