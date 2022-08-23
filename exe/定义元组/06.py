'''假设我们有一些“username@companyname.com”格式的电子邮件地址，请编写程序打印给定电子邮件地址的用户名。 用户名和公司名都只由字母组成。'''
lst = ''
for i in input():
    if i == '@':
        break
    else:
        lst += i
print(lst)

email = input().split('@')
print(email[0])