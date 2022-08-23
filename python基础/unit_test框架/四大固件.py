import unittest

class TestDemo(unittest.TestCase):
    # unittest框架的四大固件（四大夹具）
    '''
    setUp:在每个用例执行前执行的代码
    tearDown：在每个用例执行后执行的代码
    steUpClass：在所有用例执行前只执行一次，需要使用装饰器@classmethod进行声明
    tearDownClass：在所有用例执行后只执行一次，需要使用装饰器@classmethod进行声明
    '''
    # def setUp(self) -> None: # -> None表示返回值为None
    #     print('我是setup')
    # def tearDown(self) -> None:
    #     print('我是tearDown')
    @classmethod
    def setUpClass(cls) -> None:
        print('我是setUpClass')
    @classmethod
    def tearDownClass(cls) -> None:
        print('我是teardownclass')
    def testCase_1(self):
        print('测试用例1')
        self.assertEqual(0,0) # 断言，判断预期结果与实际结果是否相等
    def testCase_2(self):
        print('测试用例2')
        self.assertEqual(201102,0)
if __name__ == '__main__':
    unittest.main()