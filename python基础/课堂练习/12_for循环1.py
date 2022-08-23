'''
已知字符串str1 = "s3j_d67h_a5s624b_u"计算下划线的个数
'''
str1 = "s3j_d67h_a5s624b_u"
a = 0
for i in str1:
    if i == '_':
        a += 1
print(a)