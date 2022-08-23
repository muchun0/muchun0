'''编写一个程序，接受逗号分隔的单词序列作为输入，并将单词按字母顺序排序后以逗号分隔的序列输出。'''
# a = input('请输入内容').split(',')
# c = []
# for j in a:
#     b = ''
#     for i in range(len(j)):
#         b += min(j)
#         j = j.replace(min(j),'',1)
#     else:
#         c.append(b)
# else:
#     print(','.join(c))

lst = input().split(',')
lst.sort()
print(",".join(lst))