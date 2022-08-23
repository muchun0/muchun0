print(not True)
print(not 10) # 10可以转换成布尔值True，取反后结果为False
print(True and False) # 与运算，所有条件同时满足，结果才为真
'''短路运算'''
a = 10
b = 20
print(a and b) # a为真时，输出b的值
print(a or b) # a为真时，输出a的值，否则输出b的值
