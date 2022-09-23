def getnumber():
    number = input()
    length = len(number)
    if length == 18:
        data = number[6:14]
        if int(number[-2]) % 2 == 0:
            sex = 'feamle'
        elif int(number[-2]) % 2 != 0:
            sex = 'male'
        else:
            print('error')
        return sex
getnumber()