'''您需要编写一个程序以升序排列(名称、年龄、分数)元组，其中名称是字符串，年龄和分数是数字。 元组由控制台输入。 排序标准是:
1/基于名称排序
2/然后根据年龄进行排序
3/然后按分数排序
'''
alist = []
while True:
    a = tuple(input('请输入信息').split(','))
    if not a[0] :
        break
    else:
        alist.append(a) # 将输入内容以元组的形式，储存到列表中
# 将列表中的元素排序
alist.sort(key= lambda x:(x[0],int(x[1]),int(x[2])))
print(alist)