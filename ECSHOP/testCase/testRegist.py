import unittest
from selenium import webdriver
from common.Utils import Utils
from common.ReadData import ReadData
from Page.RegistPage import  RegistRage
import ddt
@ddt.ddt()
class TestRegist(unittest.TestCase):
    file_path = Utils().get_file_path('datas/regist_data.yaml')
    datas = ReadData(file_path).read_data_yaml()
    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get('http://localhost:8080/ecshop/eashop/upload/user.php?act=register')
    def tearDown(self) -> None:
        self.driver.close()
    @ddt.data(*datas)
    def testCase(self,data):
       actual =  RegistRage(self.driver).register(data['username'],data['email'],data['password'],data['conform_password'],data['phone'])
       self.assertEqual(data['expect'],actual)
if __name__ == '__main__':
    unittest.main()
