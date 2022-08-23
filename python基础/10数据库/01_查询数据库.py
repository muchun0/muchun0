import pymysql
# 连接数据库
con = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='426983',db='test')
cur = con.cursor() # 生成游标
cur.execute('select * from student') # 执行SQL语句
data = cur.fetchall() # 获取SQL语句结果
print(data)
cur.close() # 先关游标
con.close() # 再关数据库