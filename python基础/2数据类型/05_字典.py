student = {'name':'张三','age':18}
print(type(student))
# 1.字典的键（key）必须是不可变的类型，值（value）没有要求
# {[1]:90} 程序报错，因为使用了可变的列表作为字典的键
#2.字典的键必须是唯一的，如果发生重复，后面的键值对会覆盖前面的
print({'name': 'tom', 'age': 18, 'age': 20})

print(student['name']) # 获取键对应的值
student['age'] = 19 # 修改键对应的值
print(student)
student['sex'] = '男' # 添加新的键值对
print(student)