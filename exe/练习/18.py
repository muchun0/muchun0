'''网站要求用户输入用户名和密码才能注册。 编写一个程序来检查用户输入的密码的有效性。检查密码的条件如下:
[a-z]之间至少有一个字母
在[0-9]之间至少有一个数字
[A-Z]之间至少1个字母
[$#@]中至少一个字符
交易密码最短长度:6
交易密码的最长长度为12
您的程序应该接受一个逗号分隔的密码序列，并将根据上述标准检查它们。 匹配条件的密码将被打印出来，每个密码之间用逗号分隔。
'''

class judge():
    def __init__(self):
        for i in self:
            self.j =i

    def is_low(self):                  # Returns True  if the string has a lowercase
        if 'a'<=self.j and self.j<='z':
            return True
        else:
            return  False

    def is_up(self):                   # Returns True  if the string has a uppercase
            if 'A'<= self.j and self.j<='Z':
                return True
            else:
                return False

    def is_num(self):                  # Returns True  if the string has a numeric digit
            if '0'<=self.j and self.j<='9':
                return True
            else:
                return False

    def is_other(self):                # Returns True if the string has any "$#@"
            if self.j=='$' or self.j=='#' or self.j=='@':
                return True
            else:
                return False
