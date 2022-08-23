import unittest
from common.RequestMethod import RequestMethod
import ddt
from common.ReadData import ReadData
from common.Utils import Utils
@ddt.ddt()
class TestCons(unittest.TestCase):
    '''星座运势接口'''
    file_path = Utils().get_file_path('datas/cons_data.yaml')
    datas = ReadData(file_path).read_data_yaml()
    @classmethod
    def setUpClass(cls) -> None:
        cls.url = 'http://web.juhe.cn:8080/constellation/getAll'
    @ddt.data(*datas)
    def testCase(self,data):
        self.res = RequestMethod().getRequest(url=self.url,data=data['data'])
        self.assertEqual(data['expect'],self.res.json()['error_code'])

if __name__ == '__main__':
    unittest.main()