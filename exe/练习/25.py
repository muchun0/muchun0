'''定义一个可以将整数转换为字符串并在控制台中打印的函数。 '''
def intStr(num):
    str_num = str(num)
    print(str_num)

intStr(10)
'''定义一个函数，它可以接收两个字符串形式的整数并计算它们的和，然后在控制台中输出。'''
sum = lambda x,y:int(x)+int(y)
'''定义一个函数，它可以接受两个字符串作为输入，并将它们连接起来，然后在控制台中输出。'''
con = lambda x,y:x+y

'''定义一个函数，它可以接受两个字符串作为输入，并在控制台中以最大长度打印字符串。 如果两个字符串长度相同，则函数应逐行打印所有字符串。 '''
def maxStr(x,y):
    if len(x) > len(y):
        print(x)
    elif len(x) < len(y):
        print(y)
    else:
        print(x)
        print(y)
'''定义一个函数，它可以打印一个字典，其中键是1到20之间的数字(包括在内)，值是键的平方。'''
def dic():
    dict = {}
    for i in range(1,21):
        dict[i] = i*i
    print(dict)
'''定义一个函数，它可以生成一个字典，其中键是1到20之间的数字(包括在内)，值是键的平方。 函数应该只打印键。 '''
def dict():
    dictor={i:i*i for i in range(1,21)}
    print(list(dictor.keys()))
dict()