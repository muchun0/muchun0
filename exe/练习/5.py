'''定义一个至少有两个方法的类:

getString:从控制台输入获取一个字符串
printString:以大写形式打印字符串。
还请包含简单的测试函数来测试类方法。  '''
class GetPrint():
    # def __init__(self):
    #     self.a = ""
    def getString(self):
        self.a = input('请输入内容')
    def pringtString(self):
        print(self.a.upper())
if __name__ == '__main__':
    b = GetPrint()
    b.getString()
    b.pringtString()