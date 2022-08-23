class Student():
    school = "河北工程大学"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self):
        print(self.name+self.age+"吃饭中。。。")
    @staticmethod
    def sleep():
        print("这是一个静态方法")
    @classmethod
    def dinner(cls):
        cls.name = "馒头"
        print(cls.name)

stu1 = Student("张三",20)
print(Student.school)
stu1.drink = "二锅头"
print(stu1.drink)
stu1.sleep()
Student.dinner()
stu1.dinner()