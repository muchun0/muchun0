import unittest
from common.RequestMethod import RequestMethod
from common.ReadData import ReadData
from common.Utils import Utils
# 创建测试类，继承unittest.TestCase
class TestPhone(unittest.TestCase):
    '''手机号码归属地接口测试'''

    @classmethod
    def setUpClass(cls) -> None:
        cls.rm =RequestMethod()
        cls.url = 'http://apis.juhe.cn/mobile/get'
        cls.file_path = Utils().get_file_path('datas/phone_data.yaml')
        cls.datas = ReadData(cls.file_path).read_data_yaml()

    def testCase_1(self):
        """传入正确的参数"""
        response = self.rm.getRequest(url=self.url,
                     data=self.datas['case1']['data'])
        self.assertEqual(self.datas['case1']['expect'],response.json()['error_code'])
    def testCase_2(self):
        '''只传入key参数'''
        response = self.rm.getRequest(url=self.url,
                                data=self.datas['case2']['data'])
        self.assertEqual(self.datas['case2']['expect'], response.json()['error_code'])
if __name__ == '__main__':
    unittest.main()