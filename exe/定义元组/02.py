'''编写一个程序，可以使用map()构造一个列表，其中的元素是[1,2,3,4,5,6,7,8,9,10]中元素的平方。
编写一个程序，可以map()和filter()生成一个列表，其中的元素是[1,2,3,4,5,6,7,8,9,10]中的偶数的平方  '''
def pingfang(x):
    return x**2
lst = [1,2,3,4,5,6,7,8,9,10]
lst2 = list(map(pingfang, lst))
print(lst2)
def is_oushu(x):
    if x % 2 ==0:
        return x

# filter函数第一个参数是判断方法，如果为真，返回True,第二个参数为可迭代对象
print(list(map(pingfang, filter(is_oushu, lst))))

'''编写一个程序，它可以filter()生成一个列表，其中的元素是1到20之间的偶数(包括两个元素)。'''
lst3 = list(filter(is_oushu,list(range(1,21))))
print(lst3)
#利用lambda函数
print(list(filter(lambda x: x % 2 == 0, range(1, 21))))