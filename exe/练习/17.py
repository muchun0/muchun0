'''编写一个程序，根据控制台输入的事务日志计算银行账户的净额。 事务日志的格式如下:
D 100
W 200
D代表存款，W代表取款。
示例：
D 300
D 300
W 200
D 100
输出结果应为500
'''

balance = 0
while 4:
    operation = input('请输入日志').split(' ')
    if operation[0] == "D":
        balance += int(operation[1])
    elif operation[0] == "W":
        balance -= int(operation[1])
    else:
        break

print(balance)
# total = 0
# while True:
#     s = input().split()
#     if not s:            # break if the string is empty
#         break
#     cm,num = map(str,s)    # two inputs are distributed in cm and num in string data type
#     print(s)
#     if cm=='D':
#         total+=int(num)
#     if cm=='W':
#         total-=int(num)
#
# print(total)