'''
输入三个数,判断是否构成三角形,输出一般三角形、等腰三角形、
等边三角形
'''
a = float(input('请输入第一条边边长'))
b = float(input('请输入第二条边边长'))
c = float(input('请输入第三条边边长'))
if a + b > c and a + c > b and b + c > a :
    if a == b or b == c or a == c :
        if a == b  == c :
            print('等边三角形')
        else:
            print('等腰三角形')
    else:
        print('一般三角形')
else:
    print('不能构成三角形')



a = int(input('请输入第一条边长:'))
b = int(input('请输入第二条边长:'))
c = int(input('请输入第三条边长:'))
if a + b > c and a + c > b and b + c > a:
    if a != b != c:
        print('一般三角形')
    elif a == b == c:
        print('等边三角形')
    else:
        print('等腰三角形')
else:
    print('不构成三角形')