import pymysql
file = open('dict.txt')
db = pymysql.connect(user='root',
                     passwd='123456',
                     database='dict',
                     charset='utf8')
cur = db.cursor()
sql = "insert into d values (%s,%s);"
for i in file:
    list01 = i.split(' ',1)
    name = list01[0]
    js = list01[-1].strip()
    cur.execute(sql,[name,js])
try:
    db.commit()
except :
    db.rollback()
# 纱布衮
