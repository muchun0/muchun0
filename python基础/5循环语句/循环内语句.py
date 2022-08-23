num = 1
while num <= 10:
    print(num,end=' ')
    num += 1
    if num == 4:
        break # 终止整个循环,else中的代码不会被执行
else:
    print(num,'good bey')
print()
num1 = 1
while num1 <= 10:
    if num1 == 4:
        num1 += 1
        continue # 终止当前循环，继续下一次循环
    print(num1, end=' ')
    num1 += 1
else:
    print('good bye')