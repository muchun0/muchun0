# 文件操作，写文件
# 1、打开文件，‘w'表示覆盖原内容写入
# f = open(r'C:\Users\Administrator\Desktop\test.txt','w',encoding='utf-8')
# ’a‘ 表示在原内容追加
f = open(r'C:\Users\Administrator\Desktop\test.txt','a',encoding='utf-8')
# 2、对文件进行写操作
# f.write('你好，世界\nhello world')
f.writelines(['aaa','bbb','ccc'])
# 3、关闭文件
f.close()