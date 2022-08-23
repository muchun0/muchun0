try:
    # 要捕捉异常的代码
    18/0
except:
    # 当捕捉到异常时执行的代码
    print('有异常')
else:
    # 没有捕捉到异常时执行的代码
    print('没有异常')
finally:
    print('无论是否捕捉到异常，都会执行的代码')