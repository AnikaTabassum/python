import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = "anika",
    passwd = "hridita123",
    database = "loginDB"
    #auth_plugin='mysql_native_password'
    )
myCursor = mydb.cursor()

#myCursor.execute("CREATE DATABASE loginDB")
#myCursor.execute("SHOW DATABASES")

#for db in myCursor:
  #  print(db)
'''
myCursor.execute("CREATE TABLE questions(qid int primary key auto_increment, \
                  answer VARCHAR(80),imagePath VARCHAR(200), result VARCHAR(15))")

  
#myCursor.execute("ALTER TABLE Users ADD COLUMN Id INT AUTO_INCREMENT PRIMARY KEY")
#myCursor.execute("SHOW TABLES")

#for tables in myCursor:
    #print(tables)

'''
sql = "INSERT INTO questions(qid,answer,imagePath,result) VALUES(%s, %s, %s, %s)"
val = [
  (1, 'mango', "G:\python\img.jpg", 'null')
  
]
myCursor.executemany(sql, val)
mydb.commit()
print(myCursor.rowcount, "row was inserted.") 

myCursor.execute("SELECT * FROM questions")

myresult = myCursor.fetchall()

for records in myresult:
  print(records)

myCursor.close()
mydb.close()