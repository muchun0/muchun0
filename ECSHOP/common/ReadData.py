'''
封装读取文件数据
'''
import yaml
class ReadData():
    def __init__(self,file_path):
        self.file_path = file_path
    # 从yaml文件中读取数据
    def read_data_yaml(self):
        with open(self.file_path,'r',encoding='utf8') as fp:
            return yaml.full_load(fp)
    # 从文本文档中读取数据
    def read_data_txt(self):
        with open(self.file_path, 'r', encoding='utf8') as fp:
            return fp.read()
if __name__ == '__main__':
    print(ReadData('../datas/regist_data.yaml').read_data_yaml())