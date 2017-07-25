

import  pymysql


db = pymysql.connect("42.62.55.52",'root','123123')
cursor = db.cursor()
cursor.execute('show databases;')
data = cursor.fetchone()
print(data)
db.close()