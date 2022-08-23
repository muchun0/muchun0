a = (1,2,3)
b = ('hello',-1.23)
print(type(b))
# 元组同样支持拼接、重复、索引、切片
print(a + b)
print(a * 2)
print(b[1])
print(a[0:2])
print(type((1,))) # 一个元素的元组，需要在元素后添加逗号
# b[0] = 'world' #元组是不可变的