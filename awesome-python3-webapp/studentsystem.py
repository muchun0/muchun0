import os
import re
def main():
    while True:
        memu()
        choice = int(input('请选择'))
        if choice in list(range(8)):
            if choice == 0:
                answer = input('您确认推出系统吗？y/n')
                if answer == 'y' or answer == 'Y':
                    break
                else:
                    continue
            elif choice == 1:
                insert()
            elif choice == 2:
                serch()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()

def memu():
    print('=============学生管理系统===============')
    print('----------------功能菜单----------------')
    print('       1、录入学生信息')
    print('       2、查找学生信息')
    print('       3、删除学生信息')
    print('       4、修改学生信息')
    print('       5、排序')
    print('       6、统计学生总人数')
    print('       7、显示所有学生信息')
    print('       0、推出系统')
def insert():
    student_list=[]
    while True:
        id = input('请输入学生id（如1001）：')
        if not id:
            break
        name = input('请输入学生姓名：')
        if not name:
            break
        try:
            english = int(input('请输入英语成绩：'))
            python = int(input('请输入python成绩：'))
            java = int(input('请输入java成绩：'))
        except:
            print('您的输入有误，请重新输入')
            continue
        student_dic={'id':id,'name':name,'english':english,'python':python,'java':java}
        student_list.append(student_dic)
        save(student_list)
        answer = input('是否继续添加？y/n\n')
        if answer == 'y' or answer == 'Y':
            continue
        else:
            print('学生信息录入完毕')
            break

def save(lst):
    try:
        student_txt = open('student.txt','a',encoding='utf-8')
        for i in lst:
            student_txt.write(str(i)+'\n')
    except:
        student_txt = open('student.txt', 'w', encoding='utf-8')
        for i in lst:
            student_txt.write(str(i)+'\n')
    finally:
        student_txt.close()
def read():
    try:
       pass
    except:
        pass

def serch():
    pass
def delete():
    pass
def total():
    pass
def modify():
    pass
def sort():
    pass
def show():
    pass
if __name__ == '__main__':
    main()