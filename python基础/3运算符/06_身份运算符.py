a = b = 257
print(a == b) # 比较运算，比较的是两个对象的值是否相等
print(a is b) # 身份运算，比较的是两个对象的内存地址是否相等
'''a与b的身份运算，在pycharm中结果为True，因为pycharm中底层做了内存的优化'''