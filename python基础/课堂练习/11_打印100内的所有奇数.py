'''请写一个程序打印出 1~100 所有的奇数'''
i = 1
while i <= 100:
    if i % 2 != 0:
        print(i,end=' ')
    i += 1
num = 1
while num <= 100:
    if num % 2 == 0:
        num += 1
        continue
    print(num, end=' ')
    num += 1

