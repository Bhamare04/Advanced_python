# pip install mysql-connector
# pip install pymysql

import mysql.connector

# conn = mysql.connector.connect(
#     user='root',
#     passwd='caliber$119P',
#     host='localhost',
#     port=3306,
#     # name=''     # optional
# )

# print("Database connected successfully!!!")

import pymysql

# conn1 = pymysql.connect(
#     user='root',
#     password='caliber$119P',
#     host='localhost',
#     port=3306,
#     database='jbk'
# )

# print("Database connected successfully!!!")

# cu = conn1.cursor()

# sdata = "show databases"
# print(cu.execute(sdata))

# ctable = "create table if not exists emp (eid int, ename varchar(20))"
# cu.execute(ctable)
# print("Table created successfully!!!")

# insertdata = "insert into emp values (101, 'kartik')"
# cu.execute(insertdata)
# conn1.commit()
# print("Data inserted successfully!!!")

# insertdata = "insert into emp values (102, 'Sudhakar'), (103, 'Rajneesh'), (104, 'Sumit')"
# cu.execute(insertdata)
# conn1.commit()
# print("Data inserted successfully!!!")

# insertdata = "insert into emp values (%s, %s)"
# data = [
#     (105, 'Vaishnavi'), (106, 'Anuj'),
# ]
# cu.executemany(insertdata, data)
# conn1.commit()
# print("Data inserted successfully!!!")