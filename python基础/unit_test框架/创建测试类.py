import unittest
# 创建测试类，必须继承unittest.TestCase类
class test_demo(unittest.TestCase):
    # 创建测试用例，方法名字必须以小写的test开头
    def testCase_1(self):
        print('测试用例1')
    # 执行测试用例与光标位置有关系，放到单个用例后可以只运行单个用例
    def testCase_2(self):
        print('测试用例2')
# 程序入口
if __name__ == '__main__':
    unittest.main() # 用来执行测试用例，按照测试用例的名字的ASCII码排序后，升序运行