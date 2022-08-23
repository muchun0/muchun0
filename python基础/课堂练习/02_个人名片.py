'''
1.从键盘上输入姓名和年纪，输出字符串"我叫xxx，今年xx岁"
'''
# a = input('请输入姓名')
# b = input('请输入年纪')
# print(f'我叫{a} ，今年{b}岁')
'''在控制台依次提示用户输入：公司名称、姓名、职位、电话、邮箱，
按照以下格式输出个人名片
******************************
公司名称

姓名(职位)

电话:xxx
邮箱:xxx
******************************'''
company = input('请输入公司名称:')
name = input('请输入您的姓名:')
job = input('请输入您的职位:')
phone = input('请输入您的电话:')
email = input('请输入您的邮箱:')
flag = '*' * 30
print(f'{flag}\n{company}\n\n{name}({job})\n\n电话:{phone}\n邮箱:{email}\n{flag}')