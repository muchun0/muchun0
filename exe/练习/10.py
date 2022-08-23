'''编写一个程序，接受一个空格分隔的单词序列作为输入，并在删除所有重复的单词并按字母数字排序后输出单词。  '''
list = input('请输入内容').split(' ')
list2 = []
for i in list:
    if i not in list2:
        list2.append(i)
list2.sort()
print(' '.join(list2))