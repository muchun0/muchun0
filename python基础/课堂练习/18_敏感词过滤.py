'''
编写敏感词过滤程序，先提示用户输入内容，如果用户输入的内容中
包含特殊的字符，如“法轮功，毒品，手枪”等，将其替换成“*”，然后将
替换后的内容打印出来
'''
sensitive_word = ['法轮功','毒品','手枪']
word = input('请输入内容:')
for i in sensitive_word:
    if i in word:
        word = word.replace(i, '*' * len(i))
else:
    print(word)