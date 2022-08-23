class Student():

    # __init__构造方法/初始化方法
    def __init__(self,name,sex): # 构造方法
        self.name = name
        self.sex = sex
        print('hello')
    def studey(self):
        return f'我叫{self.name},性别{self.sex},我爱学习'
s1 = Student('张三','男') # 类的实例化时会自动调用构造方法
print(s1.studey())

s2 = Student('李四','女') # 如果构造方法具有自定义形参时，要在类后面的（）中传入实参
print(s2.studey())