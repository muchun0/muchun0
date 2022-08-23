'''编写一个程序，接受一个句子，并计算大写字母和小写字母的数量。  '''
low,up = 0,0
a = input('请输入句子')
for i in a:
    if 'a' <= i and i <= 'z':
        low += 1
    elif 'A' <= i and i <= 'Z':
        up += 1
    else:
        continue
else:
    print(f'大写字母数{up},小写字母数{low}')