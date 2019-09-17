import pymysql

# 连接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='stu',
                     charset='utf8')
# 获取游标
cur = db.cursor()

# 执行语句
sql = "insert into class values (6, 'BY', 17, 'm', 79);"
cur.execute(sql)  # 执行语句

# 提交到数据库
db.commit()

# 关闭游标数据库
cur.close()
db.close()
