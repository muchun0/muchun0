import requests
response = requests.get(url='http://apis.juhe.cn/mobile/get',
                        params={'phone':1346648,'key':'1d1afbe9b7665ce478518bb0978ef48e'})

if response.json()['error_code'] == 0:
    print('pass')
else:
    print('fail')