# 导入requests库
import requests
# 使用requests库，发送get请求，url为接口地址，params为请求参数，数据类型为字典,可以传多参，数据类型也是字典
# headers为请求头
responses = requests.get(url='https://postman-echo.com/get',
                         params={'foo1':'bar1','foo2':'bar2'},headers={'token':'hello'},timeout=3)
# 获取响应体，数据类型为字典
print(responses.json())
# 获取响应头
print(responses.headers)
# 获取响应状态码
print(responses.status_code)
