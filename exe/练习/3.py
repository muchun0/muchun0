n = int(input('请输入一个整数'))
i = 1
d = {}
while i <= n:
    d[i] = i*i
    i += 1
else:
    print(d)