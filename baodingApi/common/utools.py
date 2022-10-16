"""
封装公共工具类
"""
import os
import yaml
class Tools():
    def readYamlData(self,filepath):
        # 从yaml文件中读取数据
        with open(filepath) as fp:
            return yaml.full_load(fp)
    def getAbsPath(self, file_name):
        # 获取文件的绝对路径
        base_path = os.path.dirname(os.path.dirname(__file__))
        file_path = os.path.join(base_path, file_name)
        # file_path = os.path.abspath(file_name)
        return file_path
if __name__ == '__main__':
    print(Tools().readYamlData('/datas/createCarTypeCaseData.yml'))
