a = {1,2,3,'hello'}
print(type(a))
b = {1,9.8,False,(5,),} # 1.集合中的元素必须是不可变数据类型
print(b)
# 2.集合中的元素只能是唯一的，不允许重复
c = {1,2,3,3,3,2}
print(c)
print(type(set())) # 使用set()定义一个空集合
d = {2,4,5}
print(b - c)
print(a | d)
print(len(a)) # 求序列的长度，也就是求序列中的元素个数
