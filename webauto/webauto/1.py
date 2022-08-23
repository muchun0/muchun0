# Lambda表达式是Python中一类特殊的定义函数的形式，使用它可以定义一个匿名函数。与其它语言不同，Python的Lambda表达式的函数体只能有单独的一条语句，也就是返回值表达式语句。其语法如下： [2]
# lambda 形参列表 : 函数返回值表达式语句
# 下面是个Lambda表达式的例子：

#!/usr/bin/envpython
li=[{"age":20,"name":"def"},{"age":25,"name":"abc"},{"age":10,"name":"ghi"}]
li=sorted(li, key=lambda x:x["age"])
print(li)
# 如果不用Lambda表达式，而要写成常规的函数，那么需要这么写：
#!/usr/bin/envpython
def comp(x):
    return x["age"]
li=[{"age":20,"name":"def"},{"age":25,"name":"abc"},{"age":10,"name":"ghi"}]
li=sorted(li, key=comp)
print(li)