a = int ('50')
print(type(a))
print(float(50))
print(float('50'))
print(bool(None))
print(type(str(18)))
name ='张三'
age = 18
print('我叫' + name + ',今年' + str(age) + '岁' )
print(list('hello'))
print(list({'name':'张三','age':18})) # 字典转换结果只有键，没有值
print(True + 2) # True可以转换成整数1，Fals可以转换成整数0，python底层自动转换运算