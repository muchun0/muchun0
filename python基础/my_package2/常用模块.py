import time,copy
print(time.time()) # 时间戳
print(time.localtime())
print(time.strftime('%Y-%m-%d %H:%M:%S'))
# time.sleep(5) # 强制等待5秒
# print('hello')
'''
浅拷贝和深拷贝
1、浅拷贝：当改变原始对象中不可变数据时，不会影响拷贝对象，当改变原始对象中可变数据时，会影响拷贝对象
2、深拷贝，改变原始对象中元素的值，不会影响拷贝对象。
'''
aList1 = [2,3,'hello',[7,8]]
# aList2 = copy.copy(aList1)
# print(aList2)
# aList1[0] = 4
# print(aList1,aList2)
# aList1[-1][0] = 5
# print(aList1,aList2)
# aList3 = aList1[:]
# 以下是深拷贝
# aList3 = copy.deepcopy(aList1)
# print(aList3)
# aList1[0] = 4
# print(aList1,aList3)
# aList1[-1][0] = 5
# print(aList1,aList3)
# 两个引用的是同一个对象
aList4 = aList1
aList1[0] = 4
print(aList1,aList4)