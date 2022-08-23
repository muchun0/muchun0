import pymysql
# 连接数据库
con = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='426983',db='test')
cur = con.cursor() # 生成游标
cur.execute('insert into emp values (5,"赵六","职员",8000,1)') # 执行SQL语句
con.commit() # 提交SQL语句
cur.close()
con.close()