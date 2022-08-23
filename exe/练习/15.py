'''编写一个程序，计算a+aa+aaa+aaaa的值，将给定的数字作为a的值。'''
a = input('请输入数字')
b = 0
for i in range(1,5):
    b += int(a * i)
else:
    print(b)

# a = input()
# total,tmp = 0,str()        # initialing an integer and empty string
#
# for i in range(4):
#     tmp+=a               # concatenating 'a' to 'tmp'
#     total+=int(tmp)      # converting string type to integer type
#
# print(total)