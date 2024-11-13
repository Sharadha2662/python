import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="rkce"
)
c=mydb.cursor()
c.execute("update employee set ename=%s where eid=%s",('harsha',2))
mydb.commit()


#for inserting
#c.execute("insert into dbname values(101, 'sharadha', 1000)")
#for deleting
#c.execute("delete from dbname where eid = 103")
#for updating
#c.execute("update dbname set city = 'bangalore' where eid = 101")
