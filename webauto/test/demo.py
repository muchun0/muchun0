# for i in range(1,10):
#     print()
#     for j in range(1,i+1):
#         # if j < i :
#             print(f"{i} * {j} ={i * j} ",end='\t')
#         # elif j == i:
#         #     print(f"{i} * {j} ={i * j} ")
#         # else:
#         #     continue
import requests
import openpyxl
import json
resp = requests.get('https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=10335871588&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1')
resp.content.decode('utf-8')
comment = resp.text.replace('fetchJSON_comment98(','').replace(');','')
json_data = json.loads(comment)
for i in json_data['comments']:
    color = i['productColor']
    size = i['productSize']
    print(color,size)
wk = openpyxl.Workbook()
# sheet = wk.create_sheet()

