import requests
import unittest
import yaml
# response = requests.get(url='http://web.juhe.cn:8080/constellation/getAll',params={'key':'f662bbcb64d77fe776657851ce49d5d8','consName':
#                                                                         '金牛座','type':'today'})
# print(response.json())
class TestConsName(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.url = 'http://web.juhe.cn:8080/constellation/getAll'
    def testCase(self):
        with open(r'../data/consName_data.yaml','r',encoding='utf8') as fp:
            a = yaml.full_load(fp)
        response = requests.get(url=self.url,params=a['case1']['data'])
        self.assertEqual(a['case1']['expect'],response.json()['error_code'])
if __name__ == '__main__':
    unittest.main()