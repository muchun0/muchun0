a = 20
b = 10

def paopao(alist):
    for i in range(len(alist)-1):
        for j in range(len(alist)-1 -i):
            if alist[j] > alist[j+1]:
                alist[j],alist[j+1] = alist[j+1],alist[j]
    else:
        return alist
# 程序入口，当一个文件被当作模块被另一个文件导入时，程序入口中的代码是不会被执行的
if __name__ == '__main__':
    print(paopao([3, 2, 1]))
    print(__name__)  # 魔法变量