'''
判断一个字符串是否是"回文"，如"abccba"或"abcba"
'''
text = input('请输入字符串：')
for i in range(len(text)//2):
    if text[i] != text[-1-i]:
        print('这不是一个回文')
        break
else:
    print('这是一个回文')
