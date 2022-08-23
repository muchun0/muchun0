import unittest
import time
from testCase import testPhone,testConstellation
from common.Utils import Utils
from common.SendEmail import SendEmail
class RunMain(unittest.TestCase):
    def testCaseRun(self):
        now = time.strftime('%Y-%m-%d-%H-%M-%S')
        file_path = Utils().get_file_path('reports/'+'api-report-'+now +'.html')
        test_file_path = Utils().get_file_path('testCase')
        suite = unittest.TestSuite() # 生成测试套件
        # 加载器，加载测试用例
        # test_phone = unittest.defaultTestLoader.loadTestsFromModule(testPhone)
        # test_cons = unittest.defaultTestLoader.loadTestsFromModule(testConstellation)
        # suite.addTests([test_phone,test_cons])
        # 加载器，通过文件夹加载测试用例,用例文件的名字必须以小写的test开头
        suite.addTests(unittest.defaultTestLoader.discover(test_file_path))
        # 生成测试报告，TextTestRunner是Unittest提供的测试报告，生成的报告类型是文本文档
        # unittest.TextTestRunner(stream=open('./reports/report.txt','w',encoding='utf8'),verbosity=2).run(suite)
       # 生成HTML测试报告
        Utils().creat_report_html(file_path,'接口测试报告','2个接口，5个用例',suite)
        # 发送Email邮件
        # SendEmail().sendEmail(file_path)
if __name__ == '__main__':
    unittest.main()