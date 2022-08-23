class Animal():
    def __init__(self,kind,name):
        self.kind = kind
        self.name = name
    def shout(self):
        return f'这是{self.kind}的一种，它叫做{self.name},叫的很凶'

class Dog(Animal):
    def watch_door(self):
        return f'这是{self.kind}的一种，它叫做{self.name},能看家'
    def shout(self):
        return f'这是{self.kind}的一种，它叫做{self.name},汪汪叫的很凶'

class Cat(Animal):
    def climb_tree(self):
        return f'这是{self.kind}的一种，它叫做{self.name},爬树很快'

dog1 = Dog('哈士奇','狗蛋') # 子类实例化对象时，也会自动调用父类的构造方法
print(dog1.watch_door())
print(dog1.shout())
cat1 = Cat('波斯猫','铁蛋')
print(cat1.climb_tree())
print(cat1.shout())