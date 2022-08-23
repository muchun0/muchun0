'''
现有商品列表:
phones=[["iphone",7999],["huawei",6888],["xiaomi",3500]]
将huawei手机的价格改为5899，然后打印如下格式:
--商品列表--
iphone 7999
huawei 5899
xiaomi 3500
'''
phones=[["iphone",7999],["huawei",6888],["xiaomi",3500]]
phones[1][1] = 5899
print(f'--商品列表--\n{phones[0][0]}\t{phones[0][1]}\n{phones[1][0]}\t{phones[1][1]}\n{phones[2][0]}\t{phones[2][1]}')