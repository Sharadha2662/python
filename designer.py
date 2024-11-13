import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="designer"
)
c=mydb.cursor()
c.execute("insert into designer values(101, 'Sharadha', 1000),(102, 'Nandu',2000),(103, 'Chintu', 3000),(104, 'Motta', 4000),(105, 'Lucky', 5000),(106, 'Chandu',6000)")
mydb.commit()