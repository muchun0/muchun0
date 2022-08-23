# 自定义回文函数
def plalindrome(aStr):
    for i in range(len(aStr) // 2):
        if aStr[i] == aStr[-i - 1]:
            continue
        else:
            return f'{aStr}不是回文'
    else:
        return f'{aStr},是回文'

str1 = 'sdasf'
print(plalindrome(str1))
str2 = 'abcba'
print(plalindrome(str2))