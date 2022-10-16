import requests
from common import utools


urlList = utools.Tools().readYamlData(utools.Tools().getAbsPath('datas/urlList.yml'))
# print(urlList)
url = urlList['url']['createCarType']

caseData = utools.Tools().readYamlData(utools.Tools().getAbsPath('datas/createCarTypeCaseData.yml'))['case1']
# print(caseData)
def createCarType(jsonData,url=url):
    res = requests.post(url=url,json= jsonData).json()
    return res
# print(res.json())
if __name__ == '__main__':
    caseData = utools.Tools().readYamlData(utools.Tools().getAbsPath('datas/createCarTypeCaseData.yml'))['case1']

    print(createCarType(caseData))