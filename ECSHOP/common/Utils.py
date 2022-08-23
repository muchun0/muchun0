'''封装公共的工具类'''
import  os
from common.HTMLTestRunner import HTMLTestRunner
class Utils():
    def get_file_path(self,file_name):
        '''获取文件的绝对路径'''
        base_path = os.path.dirname(os.path.dirname(__file__))
        file_path = os.path.join(base_path,file_name)
        return file_path
    def creat_report_html(self,file_path,title,description,suite):
        with open(file_path, 'wb') as fhtml:
            HTMLTestRunner(stream=fhtml,  # 测试报告文件对象
                           verbosity=2,  # 报告日志详细等级，共0，1，2三个等级，2最详细
                           title=title,  # 报告标题
                           description=description).run(suite)  # 报告详细描述

if __name__ == '__main__':
    print(Utils().get_file_path('common/SendEmail.py'))