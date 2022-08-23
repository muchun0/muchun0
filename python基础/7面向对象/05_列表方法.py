list1 = [2,3,53,342,523,1,2]
print(list1.count(99)) # 返回元素在列表中出现的次数
print(list1.index(3)) # 返回元素在列表中第一次出现时的索引，元素不存在，则报错
print(list1.pop(1)) # 默认（-1）删除列表中最后一个元素，并且返回该元素；可以删除指定索引对应的的元素
print(list1)
list1.remove(342) # 删除第一次出现的指定元素
print(list1)
list1.clear() # 清空列表
print(list1)
list1.append(9) # 向列表中添加一个元素【掌握】
list1.append(10) # 只能在最后添加
list1.insert(0,90) # 通过指定索引，添加元素，第一个实参是索引，第二个实参是元素
list1.extend([1,2,3]) # 相当于列表的拼接，可以一次性向列表中添加多个元素【掌握】
# list1.append([1,2])
# list2 = list1.copy() # 浅拷贝，将list1列表进行复制
# list1[-1][0] = 5
# print(list1)
# print(list2)
print(list1)
list1.sort(reverse=True) # 列表冒泡排序，默认升序(False),给True是降序冒泡【掌握】
print(list1)
list1.reverse() # 列表逆序
print(list1)