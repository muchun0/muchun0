# 自定义一个手机类
class Phone():
    brand = '' # 属性其实就是变量，表示对象的静态特征
    color = ''
    # 方法其实就是函数，表示对象的动态行为
    def call(self): # self指的是对象本身
        '''
        类中的实例方法的第一个形参必须是self ，self表示对象自身，那个对象调用这个方法，self就表示那个对象
        使用对象调用实例方法时，不需要为self传入实参，python会自动传入一个对象实参。
        :return:
        '''
        return f'我是{self.color}的{self.brand}手机，我能打电话'
    def sendMessage(self):
        return  f'我是{self.color}的{self.brand}手机，我能发短信'

huawei = Phone() # 类的实例化/实例化对象，表示由类创建对象
print(huawei)
huawei.brand = 'mate40' # 对象调用类中的属性，对象.属性名
huawei.color = '绿色'
print(huawei)
print(huawei.call()) # 对象调用类中的方法，对象.方法名（）
print(huawei.sendMessage())

xiaomi = Phone()
print(xiaomi)
xiaomi.brand = '红米K30'
xiaomi.color = '黑色'
print(xiaomi.sendMessage())

# 使用类名调用类中的方法
print(Phone().sendMessage())