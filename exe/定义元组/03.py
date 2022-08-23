'''定义一个名为American的类，它有一个名为printNationality的静态方法。及其子类NewYorker'''
class American():
    def printNationality(self):
        print('I am American')
america = American()
america.printNationality()
class NewYorker(American):
    pass

