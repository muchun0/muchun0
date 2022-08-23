a = int(input('请输入一个整数'))
c = a
b = 1
while a > 0:
    # if a == 0:
    #     break
    # else:
    b = b * a
    a -= 1
print(f'{c},{b}')