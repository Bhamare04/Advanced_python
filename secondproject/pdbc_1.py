import mysql.connector

conn = mysql.connector.connect(
    user='root',
    passwd='',
    host='localhost',
    port=3306,
    name=''

)

print("Database connected successfully!")


import pymsql

conn1=pymysql.connect(
    user='root',
    password='',
    host='localhost',
    port=3306,
    database = #db name
)
print("Database connected successfully!")

cu= conn1.cursor() //cursor

sdata = "show databases"

print(cu.execute(sdata))

ctable ="create table if not exists emp(eid int,ename varchar(20))"
cu.execute(ctable)

print("Table created successfully")

insertdata = "insert into emp values(101,'kartik')"
cu.execute(insertdata)
#conn.commit()
#print("data inserted successfully")

insertdata = "insert into emp values(%s %s)"#always use %s 
data =[
    (102,'vaishnavi'),(103,'anuj')
]

cu.executemany(insertdata,data)
conn1.commit()
#print("data inserted successfully")