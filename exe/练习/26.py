'''定义一个函数，它可以生成和打印一个列表，其中的值是1到20之间的数的平方(包括这两个数)。然后函数需要打印列表中的前5个元素。
   然后函数需要打印列表中的最后5个元素。 然后，该函数需要打印列表中除前5个元素外的所有值。   '''
def listNew():
    lst = [i*i for i in range(1,21)]
    print(lst)
    print(lst[0:5])
    print(lst[-5:])
    print(lst[5:])
listNew()