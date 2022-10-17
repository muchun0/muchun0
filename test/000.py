# coding=UTF-8
import pymysql
from selenium import webdriver

movieDetails = {
        'movieName':'hahah',
        'isHot':0,
        'countNumber':123,
        'movieUrl':'hieheihie',
    }
def mysqlInsert(movieDetails):
    con = pymysql.connect(host= '127.0.0.1',user='root',port=3306,password='426983')
    cur = con.cursor()
    cur.execute('use test')
    sql = 'INSERT INTO movies values (%s,%s,%s,%s)'
    values = (movieDetails.get('movieName',None),movieDetails.get('isHot',None),movieDetails.get('countNumber',None),movieDetails.get('movieUrl',None))
    cur.execute(sql,values)
    cur.connection.commit()
    con.close()

driver = webdriver.Firefox()

def isElementExist(xpath):
    exist = True
    try:
        driver.find_element('xpath',xpath)
    except:
        exist = False
    return exist