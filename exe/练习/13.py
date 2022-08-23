'''编写一个程序，接受一个句子，并计算字母和数字的数量。'''
a = input('请输入内容')
b = c = 0
for i in a:
    try:
        i = int(i)
    except:
        b += 1
    else:
        c += 1
print(b,c)


word = input()
letter,digit = 0,0

for i in word:
    if ('a'<=i and i<='z') or ('A'<=i and i<='Z'):
        letter+=1
    if '0'<=i and i<='9':
        digit+=1

print("LETTERS {0}\nDIGITS {1}".format(letter,digit))