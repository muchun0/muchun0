'''
1.写在作业文件夹：
爱因斯坦曾出过这样一道有趣的数学题：
有一个长阶梯，若每步上2阶，最后剩1阶；若每步上3阶，最后剩2阶；
若每步上5阶，最后剩4阶；若每步上6阶，最后剩5阶；
只有每步上7阶，最后刚好一阶也不剩。
求解该阶梯至少有多少阶
'''
for i in range(999):
    if i % 2 == 1 and i % 3 == 2 and i % 5 == 4 and i % 6 == 5 and i % 7 == 0:
        print(i)
        break

i = 7
while 1:
    if i % 2 == 1 and i % 3 == 2 and i % 5 == 4 and i % 6 == 5 and i % 7 == 0:
        print(i)
        break
    i += 1