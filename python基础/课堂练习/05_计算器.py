'''
从键盘上接收两个整数,实现加减乘除计算器
'''
num1 = int(input('请输入第一个整数'))
sign = input('请输入您想要进行的计算')
num2 = int(input('请输入第二个整数'))
if sign == '+':
    print(f'{num1}+{num2}={num1 + num2}')
elif sign == '-':
    print(f'{num1}-{num2}={num1 - num2}')
elif sign == '*':
    print(f'{num1}*{num2}={num1 * num2}')
elif sign == '/':
    print(f'{num1}/{num2}={num1 / num2}')
else:
    print('您的输入有误，请重新输入')



