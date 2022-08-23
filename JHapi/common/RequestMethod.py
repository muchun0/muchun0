'''
对requests库进行二次封装，如get、post请求方法
'''
import requests
class RequestMethod():
    def getRequest(self, url, data, headers=None, verify=True):
        response = requests.get(url=url, params=data, headers=headers, verify=verify)
        return response
    def postRequest(self, url, data, dtype='json', headers=None):
        if dtype == 'form':
            response = requests.post(url=url, data=data, headers=headers)
        elif dtype == 'json':
            response = requests.post(url=url, json=data, headers=headers)
        else:
            response = None
        return response
if __name__ == '__main__':
    res = RequestMethod().getRequest(url='http://apis.juhe.cn/mobile/get',
                               data={'phone':1346648,'key':'1d1afbe9b7665ce478518bb0978ef48e'})
    print(res.json())