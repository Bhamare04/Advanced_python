import mysql.connector as msc

conn = msc.connect(
    user = "root",
    password = "abc",
    host = "locallhost",
    port =3306,
    database = 'jbk'
)

print("connection successful !!")

cu = conn.cursor()

db_name = input("enter the database name :")
dbdata = f"create  databse {db_name}"
cu.execute(dbdata)
print("database successfully created !!")

t_name = input("Enter table name :")
col_name = input("enter col name 1 :")
col_name2 = input("enter col2 name 2")

tquery f"create table{t_name} ({col_name} int ,{col_name2} varchar(20))"
cu.execute(tquery)
print("Table created successfully!!")

t_name =input("enter table name")
sid = input("enter student id")
sname = input("enter student name")

insert_query = "insert into {} values(%s,%s)".format('stud_info')
data = [(sid,sname)]

cu.executemany(insert_query,data)
conn.commit()
print("data inserted successfully !!")

# data fetching

select = "select * from stud_info"
cu.execute(select)
print(cu.fetchall())

select = "select * from {t_name} where sid={}".format(t_name,sid)
cu.execute(select)
print(cu.fetchone())

#update query

t_name =input("enter table name")
col_name = input("enter col name :")
updated_name =input("enter updated name")
sid = input("enter student id")

update_query ="update {} set{}=%s where sid=%s".format(t_name,col_name)
data = [(updated_name,sid)]
cu.executemany(update_query,data)
conn.commit()
print("data updated successfully")