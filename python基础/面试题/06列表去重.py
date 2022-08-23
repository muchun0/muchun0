aList = [2,3,3,5,11,78,11,11]
b = []
# for i in aList: # for 循环是按照索引进行，aList变化，索引发生变化
#     print(i)
#     if aList.count(i) >=1:
#         b.append(i)
#         print(aList)
#         j = 0
#         while j < aList.count(i):
#             aList.remove(i)
#             print(aList)
for i in aList:
    if i not in b:
        b.append(i)
else:
    print(b)
