# i = '*'
# j = 0
# while j in range(4):
#     print(i)
#     i = i + '*'
#     j += 1
# a = 1
# while a <= 4:
#     print('*' * a)
#     a += 1
'''
   *
  ***
 *****
*******
'''
# i = 3
# j = 1
# while i >= 0:
#     print(' ' * i + '*' * j)
#     i -= 1
#     j += 2
num = 1
count = 10  # 循环次数
while num <= count:
    print(' ' * (count - num) + '*' * (2 * num - 1))
    num += 1