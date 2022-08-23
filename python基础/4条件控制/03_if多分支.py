score = int(input('请输入分数：'))
# 当某个表达式为True时，整个if多分支语句就会结束，不会继续检查后面的表达式
if  90 <= score and score <= 100: # 可以写成 90 <= score <= 100
    print('优秀')
elif score < 90 and score >= 80:
    print('良好')
elif score < 80 and score >= 60:
    print('一般')
elif score <60 and score >= 0:
    print('不及格')
else:
    print('分数有误，请重新输入')