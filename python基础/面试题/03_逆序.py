'''
将一个列表[9,6,5,7,4,1]逆序输出
'''
list = [9,6,5,7,4,1]
# for i in range(len(list)):
#     if i < len(list)//2:
#         list[i],list[len(list)-i-1] = list[len(list)-i-1],list[i]
# else:
#     print(list)
for i in range(len(list)//2):
    list[i], list[ - i - 1] = list[ - i - 1], list[i]
else:
    print(list)