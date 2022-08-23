from django.http import HttpResponse
from django.shortcuts import render, redirect
import datetime
import pymysql
def hello(request):
    return HttpResponse("Hello world ! ")
# def runoob(request):
#     context          = {}
#     context['hello'] = 'Hello World!'
#     return render(request, 'runoob.html', context)
#变量
# def runoob(request):
#   views_name = "菜鸟教程"
#   return  render(request,"runoob.html", {"name":views_name})
#列表
# def runoob(request):
#     views_list = ['张三','李四','王五','赵六']
#     return  render(request,'runoob.html',{'name':views_list})
# def runoob(request):
#     views_dict = {'Jhon':29,'lilei':18,'hanmeimei':'femal'}
#     return render(request,'runoob.html',{'name':views_dict})
# #data过滤器
# def runoob(request):
#     context = {'name':datetime.datetime.now()}
#     return render(request,'runoob.html',context)
#省略展示：truncatechars
# def runoob(request):
#     views_str = "菜鸟教程"
#     return render(request,'runoob.html',{'name':views_str})
#safe:将字符串标记为安全，取消转义
# def runoob(request):
#     views_str = "<a href='https://www.runoob.com/'>点击跳转</a>"
#     return render(request, "runoob.html", {"name": views_str})
#if/else语句
# def runoob(request):
#     view_score = 100
#     return render(request,"runoob.html",{'name':view_score})
# def runoob(request):
#     view_list = [100,90,80,70,60,50]
# #     return render(request,"runoob.html",{'name':view_list})
# def runoob(request):
#     view_divt = {'jhon':19,'lilei':28,'hanmeimei':99}
#     return render(request,'runoob.html',{'name':view_divt})
# def runoob(request):
#     name = request.GET.get("name")
#     return HttpResponse('姓名：{}'.format(name))
# def runoob(request):
#     # return HttpResponse("菜鸟教程")
#     return HttpResponse("<a href='https://www.runoob.com/'>菜鸟教程</a>")
# def runoob(request):
#     name = '菜鸟教程'
#     return render(request,'runoob.html',{"name":name})
# def runoob(request):
#     return redirect("/search_form/")
def index(request, year, month):
    print(year,month) # 一个形参代表路径中一个分组的内容，按关键字对应匹配
    return HttpResponse('菜鸟教程')
def test(request):
    conn=pymysql.connect(user='root',password='426983',host='127.0.0.1',port=3306)
    cur = conn.cursor()
    cur.execute('use runoob;')
    data = cur.execute('select name from testmodel_test where id = 1;')
    print(data)
    cur.close()
    conn.close()
    return HttpResponse(data)
