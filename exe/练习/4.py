# input输入的都是字符串，调用字符串的方法splist，将字符串转化成列表，字符串用逗号分隔，代表转换成列表时不同的元素
lst = input().split(',')
tpl = tuple(lst)
print(lst)
print(tpl)


