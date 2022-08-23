username = 'aaabbbcccddd'
if len(username) <= 10:
    print('注册成功')
else:
    raise Exception('用户名长度超过10，注册失败')