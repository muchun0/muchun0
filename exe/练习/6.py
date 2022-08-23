'''编写一个程序，根据给定的公式计算并打印值:

Q = [(2c D)/H]的平方根

C和H的固定值如下:

C是50。 H是30。

D是变量，它的值应该以逗号分隔的序列输入到程序中。 让我们假设下面的逗号分隔输入序列是给程序的:  '''

list = input('请输入数字').split(',')
list2 = []
for i in range(len(list)):
    num = ((int(list[i])*100)/30) ** 0.5
    num = int(num)
    str_num = str(num)
    list2.append(str_num)
else:
    print(','.join(list2))

# from math import sqrt # import specific functions as importing all using *
#                       # is bad practice
#
# C,H = 50,30
#
# def calc(D):
#     return sqrt((2*C*D)/H)
#
# D = [int(i) for i in input().split(',')] # splits in comma position and set up in list
# D = [int(i) for i in D]   # converts string to integer
# D = [calc(i) for i in D]  # returns floating value by calc method for every item in D
# D = [round(i) for i in D] # All the floating values are rounded
# D = [str(i) for i in D]   # All the integers are converted to string to be able to apply join operation
# print(D)
# print(",".join(D))