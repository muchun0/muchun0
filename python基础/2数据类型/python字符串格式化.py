name = '张三'
age = 18
height = 1.89 # 四舍六入五成双
print('我叫%s,今年%d岁'%(name,age))
print('我叫%s,今年%d岁，身高%.2f米'%(name,age,height))
print(f'我叫{name}，今年{age}岁，身高{height}米') # f字符串格式化，python3.6版本新加入的