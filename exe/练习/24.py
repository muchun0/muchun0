'''Python有许多内置函数，如果您不知道如何使用它，您可以在线阅读文档或查找一些书籍。 但是Python对于每个内置函数都有一个内置的文档函数。

请写一个程序打印一些Python内置函数文档，比如abs()， int()， raw_input()

并为自己的功能添加文档  '''
print(str.__doc__)
print(sorted.__doc__)

def pow(n,p):
    '''
    param n: This is any integer number
    param p: This is power over n
    return:  n to the power p = n^p
    '''

    return n**p

print(pow(3,4))
print(pow.__doc__)
