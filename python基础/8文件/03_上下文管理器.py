# 上下文管理器，省去了手动调用关闭文件的操作，会自动关闭文件
with open(r'C:\Users\Administrator\Desktop\test.txt','r',encoding='utf-8') as f:
    print(f.read())
