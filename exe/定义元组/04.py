'''定义一个名为Circle的类，可以用半径来构造。 Circle类有一个可以计算面积的方法。'''
class Circle():
    def __init__(self,r):
        self.r  = r
    def mianji(self):
        return 3.14*self.r**2


print(Circle(2).mianji())
'''定义一个名为Rectangle的类，它可以由长度和宽度构造。 矩形类有一个方法可以计算面积。'''
class Rectangle():
    def __init__(self,l,h):
        self.l = l
        self.h = h
    def area(self):
        return self.l*self.h


print(Rectangle(3, 4).area())
'''定义一个名为Shape的类及其子类Square。 Square类有一个init函数，它以长度作为参数。 这两个类都有一个area函数，可以打印形状的区域，形状的区域默认为0。  '''
class Shape():
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self,length = 0):
        Shape.__init__(self)
        self.length = length

    def area(self):
        return self.length*self.length

Asqr = Square(5)
print(Asqr.area())      # prints 25 as given argument

print(Square().area())  # prints zero as default area
'''请引发RuntimeError异常。'''
raise RuntimeError('something wrong')