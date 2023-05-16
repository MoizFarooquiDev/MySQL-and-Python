import mysql.connector as sql
mydb=sql.connect(
    host="localhost",
    user="root",
    passwd="Poi1poi1#",
    database="testdb"
    )
print(mydb)

mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE testdb")
mycursor.execute("SHOW DATABASES")

for db in mycursor:
    print(db)
    
mycursor.execute("CREATE TABLE Books(Book_ID Integer(2),Book_Name Varchar(100), Publisher Varchar(20),Edition Varchar(20), Number_of_pages Integer(5), Sales Varchar(5), City Varchar(20),Price Integer(5))")
for tb in mycursor:
    print(tb)
 
sqlformula="INSERT INTO Books(Book_ID,Book_Name,Publisher,Edition,Number_of_pages,Sales,City,Price) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
book1=(12,"Harry Potter","Warner Bros","5th",650,"HIGH","London",5000)
book2=(13,"Lost Time ","Warner Bros","5th",650,"HIGH","London",5000)
book3=(14,"Ulyses","James Joyce","2nd",210,"HIGH","Newyork",7500)
book4=(15,"One Hundred Years","Gabriel","2nd",650,"LOW","Washington",4567)
book5=(16,"Mobby Dick","Herman","3rd",650,"HIGH","Barcelona",6235)
book6=(17,"War And Peace","Troy","5th",650,"LOW","New York",2000)
book7=(18,"Hamlet","Shakespeare","7th",650,"LOW","New Jersey",4530)
book8=(19,"Divine Comedy","Dante","5th",650,"HIGH","London",7800)
book9=(21,"Pride and Prejudice","Jane","4th",650,"LOW","Frankfurt",4590)
book10=(22,"Karachi","Moiz","1st",650,"HIGH","Karachi",5500)

mycursor.execute(sqlformula,book1)
mycursor.execute(sqlformula,book2)
mycursor.execute(sqlformula,book3)
mycursor.execute(sqlformula,book4)
mycursor.execute(sqlformula,book5)
mycursor.execute(sqlformula,book6)
mycursor.execute(sqlformula,book7)
mycursor.execute(sqlformula,book8)
mycursor.execute(sqlformula,book9)
mycursor.execute(sqlformula,book10)

mydb.commit()

import pandas
query= "select * from Books"

pdf = pandas.read_sql(query, mydb)
pdf

query="SELECT Book_Name,Price from Books WHERE(SELECT MAX(Price) FROM Books) LIMIT 1"
pdf=pandas.read_sql(query,mydb)
pdf

query="SELECT * FROM Books WHERE City='London'"
pdf=pandas.read_sql(query,mydb)
pdf



