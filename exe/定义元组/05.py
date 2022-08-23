'''编写一个函数来计算5/0，并使用try/except来捕获异常。  '''
try:
    x = int(input())
    y = int(input())
    print(x/y)
except:
    print('您的输入有误')
'''定义一个自定义异常类，它将字符串消息作为属性。'''
class CustomException(Exception):
    """Exception raised for custom purpose

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message


num = int(input())

try:
    if num < 10:
        raise CustomException("Input is less than 10")
    elif num > 10:
        raise CustomException("Input is grater than 10")
except CustomException as ce:
    print("The error raised: " + ce.message)