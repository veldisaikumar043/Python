import mysql.connector;
conn=mysql.connector.connect(host='localhost',database='saikumar',user='root',password='abc@1234')
if conn.is_connected():
    print("connected to saikumar DB")
cursor1=conn.cursor()
# cursor1.execute("select * from emp1 order by emp1.empSal desc")
cursor1.execute("delete from emp1 where empName like 'a%'")
print("employee deleted whose name start with a")
cursor1.execute("select * from emp1 order by emp1.empSal desc")
rows=cursor1.fetchall()
print("total no of records : ",cursor1.rowcount)
for row in rows:
    print(row)
print()

# try:
#     cursor1.execute("UPDATE emp1 SET empSal=25000 WHERE empId=1");
#     cursor1.execute("UPDATE emp1 SET empSal=25000 WHERE empId=2");
#     conn.commit()
#     print(" employee details updated")
# except:
#     conn.rollback()
#     print(" employee details not updated")

cursor1.close()
conn.close