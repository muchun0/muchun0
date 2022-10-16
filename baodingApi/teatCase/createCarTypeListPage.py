import requests
from common import utools

urlList = utools.Tools().readYamlData(utools.Tools().getAbsPath('datas/urlList.yml'))
# print(urlList)
url = urlList['url']['createCarTypeListPage']

caseData = utools.Tools().readYamlData(utools.Tools().getAbsPath('datas/createCarTypeListPageData.yml'))['case1']
# print(caseData)
def createCarTypeListPage(jsonData,url=url):
    res = requests.post(url=url,json=jsonData).json()
    return res
# print(res.json())
if __name__ == '__main__':
    caseData = utools.Tools().readYamlData(utools.Tools().getAbsPath('datas/createCarTypeListPageData.yml'))['case1']

    print(createCarTypeListPage(caseData))