'''
已知两个列表,将list1中不属于list2的元素打印出来
list1 = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
list2 = ["Sun","Mon","Tue","Thu","Sat"]
'''
list1 = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
list2 = ["Sun","Mon","Tue","Thu","Sat"]
for i in list1:
    if i not in list2:
        print(i)
