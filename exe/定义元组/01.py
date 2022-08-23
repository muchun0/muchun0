'''定义一个函数，它可以生成并打印一个元组，其中的值是1到20之间的数的平方(包括这两个数)。'''
def toup():
    tup = tuple([i**2 for i in range(1,21)])
    print(tup)
'''对于给定的元组(1,2,3,4,5,6,7,8,9,10)，编写一个程序，在一行中输出前半部分值，在一行中输出后半部分值。 
 生成并输出另一个元组，其值是给定元组(1,2,3,4,5,6,7,8,9,10)中的偶数'''
tup = (1,2,3,4,5,6,7,8,9,10)
a = len(tup)/2
print(tup[:int(a)],tup[int(a):])
lst = []
for i in tup:
    if i % 2 == 0:
        lst.append(i)
print(tuple(lst))
'''写一个程序，接收一个字符串作为输入，如果字符串是“Yes”或“yes”或“YES”，则输出“Yes”，否则输出“No”。  '''
lst = ["Yes","YES","yes"]
a = input('请输入字符串')
if a in lst :
    print('Yes')
else:
    print('No')