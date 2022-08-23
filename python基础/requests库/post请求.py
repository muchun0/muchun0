import requests
# requests发送post请求时，使用data参数名，传递的数据为form表单
# response = requests.post(url='https://postman-echo.com/post',data={'foo1':'bar1','foo2':'bar2'})
# requests发送post请求时，使用json参数名，传递的数据为json表单
response = requests.post(url='https://postman-echo.com/post',json={'foo1':'bar1','foo2':'bar2'})
print(response.json())