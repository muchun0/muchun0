import unittest
from selenium import webdriver
from Page.LoginPage import LoginPage
from common.ReadData import ReadData
from common.Utils import Utils
class testLogin(unittest.TestCase):
    file_path = Utils().get_file_path('datas/login_data.yaml')
    datas = ReadData(file_path).read_data_yaml()
    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get('http://localhost:8080/ecshop/eashop/upload/user.php')
    def tearDown(self) -> None:
        self.driver.close()
    def testCase_1(self):
        actual = LoginPage(self.driver).login(self.datas['case1']['username'],self.datas['case1']['password'])
        self.assertEqual(self.datas['case1']['expect'],actual)
    def testCase_2(self):
        actual = LoginPage(self.driver).login(self.datas['case2']['username'],self.datas['case2']['password'])
        self.assertEqual(self.datas['case2']['expect'], actual)
if __name__ == '__main__':
    unittest.main()
