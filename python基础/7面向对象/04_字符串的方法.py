aStr = '  hd_djs  _djoas_ABC   '
print(aStr.count('_')) # 返回指定字符串在某个字符串中出现的次数（ctrl+光标移动到函数位置，可以看到参考，冒号后边是提示类型）
print(aStr.index('d')) # 返回指定元素在字符串中第一次出现的索引，如果未找到元素，则程序报错
print(aStr.find('z')) # 返回指定元素在字符串中第一次出现的索引,如果未找到元素，则返回-1
print(aStr.split('_')) # 按照指定元素切割字符串，返回列表【掌握】
name = '张三'
age = 18
print('我叫{0},今年{1}岁，我有个同学也叫{0}'.format(name,age)) # 字符串的格式化，0，1是索引，可以省略
print(aStr.upper()) # 将字符串中的所有小写字母都变成大写字母，但是生成的是一个新的字符串
print(aStr.lower()) # 将字符串中的所有大写字母都变成小写字母
print(aStr.strip()) # 去除字符串左右两边指定的字符串，默认是去除空格
print(aStr.lstrip()) # 去除左边指定的字符串
print(aStr.rstrip()) # 去除右边指定的字符串
print(aStr.replace('j','a',1)) # 替换字符串中的元素【掌握】
print(aStr.join(['www','baidu','com'])) # 使用指定的字符串将序列中的所有元素连接到一起【掌握】
print(aStr.isdigit()) # is开头的就是用来判断的