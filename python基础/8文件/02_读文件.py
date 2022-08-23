f = open(r'C:\Users\Administrator\Desktop\test.txt','r',encoding='utf-8')
# print(f.read()) # 一次性将文件中的所有数据全部读出
# print(f.readline())
# print(f.readline())
# while 1:
#     a = (f.readline())
#     if a != '':
#         print(a)
#     else:
#         break
'''data = f.readline()
# 使用readline方法（每次读取一行内容）实现读取文件中的全部内容
while data:
    print(data.rstrip('\n'))
    data = f.readline()'''
print(f.readlines()) # 读取文件中的全部内容，返回一个列表，每一行是一个元素
f.close()
