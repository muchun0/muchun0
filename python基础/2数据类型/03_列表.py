fruit = ['apple','banana','orange','mango','pear']
print(type(fruit))
a = ['hello',20,True,[1,2]]
b = [[1.2],[3,4,5]] # 嵌套列表
print(a + b) # 列表拼接
print(a * 2) # 列表重复
print(a[2]) # 列表索引，返回结果数据类型是元素本身的类型
print(a[1:3]) # 列表切片，返回结果仍是列表
fruit[2] = 'peach' # 将orange元素改为peach
print(fruit)
b[1][2] = 6 # 嵌套列表需要多个索引
print(b)