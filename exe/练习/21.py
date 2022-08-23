'''机器人从原点(0,0)开始在平面上运动。 机器人可以按照给定的步骤向上下左右移动。 机器人运动轨迹如下所示:
上5
下3
左3
右2
方向后面的数字是步骤。 请编写一个程序来计算从当前位置经过一个序列的移动和原始点的距离。
如果距离是一个浮点数，那么就输出最近的整数。 示例:如果以下元组作为程序的输入:
UP 5
DOWN 3
LEFT 3
RIGHT 2
输出 ： 2
'''
x = 0
y = 0
atuple = (x,y)
alist = []
while True:
    step = input('请输入操作步骤').split(' ')
    if  not step[0]:
        break
    else:
        alist.append(step)
for i in alist:
    if i[0] == 'UP':
        y += int(i[1])
    elif i[0] == 'DOWN':
        y -= int(i[1])
    elif i[0] == 'LEFT':
        x -= int(i[1])
    elif i[0] == 'RIGHT':
        x += int(i[1])
distence = x ** 2 + y ** 2
print(f'{int(distence**0.5)}')

