# 生成1-9的列表，不包含10
print(list(range(1,10)))
print(list(range(10))) # 生成0 - 9 的列表，省略开始数字，默认从0开始
print(list(range(1,11,2))) # 步长为2

for i in range(20):
    print(i,end=' ')
print()
student = ['tom','lily','chris','john']
for i in range(len(student)):
    print(student[i])