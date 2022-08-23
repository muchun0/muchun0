import unittest
import time
from common.Utils import Utils
from common.SendEmail import SendEmail
class RunMain(unittest.TestCase):
    def testRunner(self):
        now = time.strftime('%Y-%m-%d-%H-%M-%S')
        file_path = Utils().get_file_path('reports/' + 'ecshop-report-' + now + '.html')
        suite = unittest.TestSuite()
        suite.addTests(unittest.defaultTestLoader.discover(Utils().get_file_path('testCase')))
        Utils().creat_report_html(file_path,'ecshop测试报告','2个页面 4个用例',suite)
        # 发送Email邮件
        SendEmail().sendEmail(file_path)
if __name__ == '__main__':
    unittest.main()