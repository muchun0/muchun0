from teatCase import createCarType,createCarTypeListPage
import unittest
from ddt import ddt,data
from common import utools

@ddt
class Main(unittest.TestCase):

    @data(*utools.Tools().readYamlData('datas/createCarTypeCaseData.yml'))
    def testCase_1(self,data):
        datas = utools.Tools().readYamlData('datas/createCarTypeCaseData.yml')
        res = createCarType.createCarType(datas[data])
        unittest.TestCase().assertEqual('成功',res['Msg'])
    @data(*utools.Tools().readYamlData('datas/createCarTypeListPageData.yml'))
    def testCase_2(self,data):
        datas = utools.Tools().readYamlData('datas/createCarTypeListPageData.yml')
        res = createCarTypeListPage.createCarTypeListPage(datas[data])
        unittest.TestCase().assertEqual('成功', res['Msg'])
if __name__ == '__main__':
    unittest.main()