student = ['张三','李四','王五','赵六']
'''
for循环是循环一个迭代对象（任何序列），这个迭代对象中有多少个元素，就会循环多少次，
每次循环时，都会将迭代对象中的元素取出来，赋值给迭代变量（就是一个变量名，习惯用i来表示）
'''
for i in student:
    print(i)
else:
    print('hello')

aList = [[1,2],[3,4],[5,6]]
for i in aList:
    for j in i:
        if j == 4:
            break
        print(j)
    if j == 4:
        break

