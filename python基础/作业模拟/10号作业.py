# name = input('请输入用户名')
# password = input('请输入密码')
# if name == 'root' and password == '123456':
#     print('登录成功')
# else:
#     print('登陆失败')
'''2. 输入两个数,比较它们的大小并输出其中较大者,'''
a = int(input('请输入第一个数'))
b = int(input('请输入第二个数'))
if a == b :
    print('两个数相等')
else:
    print(max(a,b))
'''3. 提示用户"请输入公交卡余额:"
1)如果公交卡余额大于等于5就可以乘车，否则打印"余额不足,请及时充值"
2)上车后,提示用户"请输入空座位:",如果输入的座位大于0,
则打印"有空座位,可以坐下",否则打印"没有座位,请您抓稳扶好"'''
# balance = int(input('请输入公交卡余额'))
# if balance >= 5 :
#     sit = int(input('请输入空座位'))
#     if sit > 0 :
#         print('有空座位，可以坐下')
#     else:
#         print('没有座位，请您抓稳扶好')
# else:
#     print('余额不足，请及时充值')
'''4. person={"张三":{"age":20,"sex":"男"},
          "李四":{"age":18,"sex":"女"},
          "王五":{"age":19,"sex":"男"}}
通过键盘输入姓名,然后打印出该人的信息,
如输入"李四"则输出"姓名李四,年龄18,性别女"'''
# person={"张三":{"age":20,"sex":"男"},
#           "李四":{"age":18,"sex":"女"},
#           "王五":{"age":19,"sex":"男"}}
# name = input('请输入姓名：')
# if name in person:
#     print(f'姓名{name},年龄{person[name]["age"]},性别{person[name]["sex"]}')
# else:
#     print('没有该名学生')