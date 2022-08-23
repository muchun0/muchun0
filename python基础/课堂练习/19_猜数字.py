'''
猜数字游戏，系统生成一个1-100之间的随机整数。
从键盘输入一个整数，与系统生成的整数进行比较，如果大于系统生成的整数，则提示输大了，然后重新再输入一个整数；如果小于系统生成的整数，则提示输小了，然后重新再输入一个整数；如果等于系统生成的整数，则提示猜对了，整个程序结束。
一共7次机会，7次没猜对，整个程序也结束。
'''
import random
computer = random.randint(1,100)
print(computer)
for i in range(7):
    num = int(input('请输入你猜测的数字'))
    if num == computer:
        print('恭喜你，猜对了')
        break
    elif num > computer:
        print('猜大了')
        continue
    else:
        print('猜小了')
        continue


computer = random.randint(1,100)
for i in range(7):
    num = int(input('请猜数字:'))
    if num > computer:
        print('猜大了')
    elif num < computer:
        print('猜小了')
    else:
        print('恭喜你猜对了')
        break
else:
    print('很遗憾，次数用尽，下次努力')